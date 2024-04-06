from core.main import cli, config, app
from core.support.service_provider import ServiceProvider

import shutil
import importlib
import os
import click

destination_directory = "./config/"

@cli.command("publish")
@click.argument('group')
def package_test(group: str):
    paths_to_publishes = {}
    for service_provider in app._service_providers:
        service_provider_name = service_provider.__class__.__name__
        paths_to_publish = ServiceProvider.paths_to_publish(service_provider.__class__, group)
        if paths_to_publish:
            paths_to_publishes[service_provider_name] = paths_to_publish
    print(paths_to_publishes.items(), "\n\n")
    print("Available paths to publish:")
    
    print_list(paths_to_publishes)
    selected_paths = input("\nEnter the numbers of paths to publish (comma-separated): ")
    selected_paths = [int(index) for index in selected_paths.split(',')]

    index = 1
    for provider_name, paths in paths_to_publishes.items():
        if index in selected_paths:
            module_name, publish_path = next(iter(paths.items()))
            # В этом примере просто выводится сообщение о публикации выбранного пути
            print(f"\nPublishing {module_name} from {provider_name}...")

            module = importlib.import_module(module_name)
            publish(module, publish_path)
        index += 1
    
def print_list(paths_to_publishes: dict):
    index = 1
    for provider_name, paths in paths_to_publishes.items():
        module_name, publish_path = next(iter(paths.items()))
        print(f"\nFrom {provider_name}:")
        print(f"{index}. {publish_path}")
        index += 1
            

def convert_module_to_path(text: str):
    # Заменяем точки на слэши и добавляем расширение .py
    python_path = "./" + text.replace(".", "/") + ".py"
    return python_path


def publish(module, publish_file):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    publish_path = convert_module_to_path(publish_file)
    shutil.copy(module.__file__, publish_path)

    print('Create file: ' + publish_path)
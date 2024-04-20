import asccore.support.auth.model as auth_model

class PersonalAccessToken(auth_model.PersonalAccessToken):
    class Meta(auth_model.PersonalAccessToken.Meta):
        pass

    class QuerySet(auth_model.PersonalAccessToken.QuerySet):
        pass
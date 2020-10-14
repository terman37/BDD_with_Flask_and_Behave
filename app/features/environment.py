from src.main import myapi


def before_feature(context, feature):
    myapi.testing = True
    context.client = myapi.test_client()


def after_feature(context, feature):
    pass

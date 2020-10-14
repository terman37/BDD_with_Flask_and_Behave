from behave import given, when, then


@given('my flask app is running')
def step_impl_given(context):
    assert context.client


@when('my app gets a GET request "{qry}"')
def step_impl_when(context, qry):
    context.page = context.client.get(qry, follow_redirects=True)
    assert context.page


@then('the response should be "{response}" with status "{status}"')
def step_impl_then(context, response, status):
    assert context.page.status == status
    assert str(context.page.json['answer']) == response

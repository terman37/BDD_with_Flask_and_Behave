Feature: Testing Flask

    Scenario: Test home page
        Given my flask app is running
        When my app gets a GET request "/"
        Then the response should be "hello world" with status "200 OK"

    Scenario: Test double page
        Given my flask app is running
        When my app gets a GET request "/double/?x=2"
        Then the response should be "4" with status "200 OK"
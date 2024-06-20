Feature: Verify status code of API endpoint

    Scenario Outline: Verify status code of a GET request to a given URL <url>
        Given I send a GET request to the endpoint "<url>"
        Then the response status code should be "<Status>"
        Then kill the request

        Examples:
            | url              | Status |
            | api/users?page=2 | 200    |

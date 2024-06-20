Feature: Verify Delete method is successfull

    @smokeTest
    Scenario Outline: Delete the ID
        Given User navigates to delete "<URL>"
        When user submits the delete request
        Then status should be "200"

        Examples:
            | URL             |
            | api/v1/delete/1 |
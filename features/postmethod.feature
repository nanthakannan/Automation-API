Feature: Verify Post methos is successfull

    @smokeTest
    Scenario Outline: Create the Name
        Given User navigates to "<URL>"
        Given user enters with "<Name>" and "<job>"
        When user submits the request
        Then status should be "201"

        Examples:
            | URL       | Name    | job  |
            | api/users | tester5 | Lead |
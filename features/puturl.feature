Feature: Verify Put method is successfull

    @smokeTest
    Scenario Outline: Update the Name
        Given User navigates to "<URL>"
        Given user update with "<Name>" and "<job>"
        When user submits the put request
        Then status should be "200"

        Examples:
            | URL         | Name    | job    |
            | api/users/2 | tester9 | Leader |
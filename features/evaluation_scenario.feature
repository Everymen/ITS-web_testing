Feature: Evaluation Scenario
  Scenarios concerning evaluation scenarios

  Background:
    Given a web browser is at VALU3S home page

#  Rule: Permissions to perform an operation granted
#    Rule: All required fields are filled in
      Scenario: 1. Create evaluation scenario
        Given user is successfully logged in w/ permissions to create
        Given user selected "Add new...", "Evaluation Scenario" options
        Given user filled in all required fields
        When user clicks "Save" button
        Then "Item created" information box pops up
        And all fields filled in by user are saved (item created)
        And item state is private

#    Rule: All required fields are not filled in
      Scenario: 2. Create evaluation scenario
        Given user is successfully logged in w/ permissions to create
        Given user selected "Add new...", "Evaluation Scenario" options
        Given user did not filled in all required fields
        When user clicks "Save" button
        Then "There were some errors" error box pops up
        And all required fields not filled in are highlighted
        And item is not created

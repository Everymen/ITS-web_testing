Feature: Item
  Scenarios concerning items
  
  Background:
    Given a web browser is at VALU3S home page

#  Rule: Permissions to perform an operation granted
#    Rule: All required fields are filled in
      Scenario: 17. Edit item (button version)
        Given user is successfully logged in w/ permissions to edit
        Given user selected "Contents" option
        Given user clicked on "Edit" button of desired item
        Given user edited desired fields w/ all required fields filled in
        When user clicks "Save" button
        Then "Changes saved" information box pops up
        And all fields edited by user are saved

      Scenario: 18. Edit item (option version)
        Given user is successfully logged in w/ permissions to edit
        Given user navigated to desired item
        Given user clicked on "Edit" option
        Given user edited desired fields w/ all required fields filled in
        When user clicks "Save" button
        Then "Changes saved" information box pops up
        And all fields edited by user are saved

#    Rule: All required fields are not filled in
      Scenario: 19. Edit item (button version)
        Given user is successfully logged in w/ permissions to edit
        Given user selected "Contents" option
        Given user clicked on "Edit" button of desired item
        Given user edited desired fields w/o all required fields filled in
        When user clicks "Save" button
        Then "There were some errors" error box pops up
        And all required fields not filled in are highlighted
        And all fields edited by user are not saved

      Scenario: 20. Edit item (option version)
        Given user is successfully logged in w/ permissions to edit
        Given user navigated to desired item
        Given user clicked on "Edit" option
        Given user edited desired fields w/o all required fields filled in
        When user clicks "Save" button
        Then "There were some errors" error box pops up
        And all required fields not filled in are highlighted
        And all fields edited by user are not saved
    
    Scenario: 21. Delete item
      Given user is successfully logged in w/ permissions to delete
      Given user selected "Contents" option
      Given user selected desired items for deletion
      Given user clicks "Delete" button
      When user clicks "Yes" button
      Then "Successfully delete items" information box pops up
      And items are deleted

    Scenario: 22. Change item state
      Given user is successfully logged in w/ permissions to change state
      Given user navigated to desired item
      When user selected desired item state from option menu
      Then "Item state changed" information box pops up
      And item state changed to user's desired state

#  Rule: Permissions to perform an operation not granted
    Scenario: 23. Edit item
      Given user is successfully logged in w/o permissions to edit
      Given user selected "Contents" option
      When user clicks "Edit" button of desired item
      Then "Insufficient Privileges" page pops up

    Scenario: 24. Delete item
      Given user is successfully logged in w/o permissions to delete
      Given user selected "Contents" option
      Given user selected desired items for deletion
      Given user clicks "Delete" button
      When user clicks "Yes" button
      Then "Permission denied" information box pops up
      And items are not deleted

    Scenario: 25. Change item state
      Given user is successfully logged in w/o permissions to change state
      Given user navigated to desired item
      When user selected desired item state from option menu
      Then "Insufficient Privileges" page pops up
      And item state is unchanged

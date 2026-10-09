Feature: Movie theater seat booking

  Scenario: Book an available seat
    Given a movie exists
    And an available seat exists
    And a user exists
    When the user books the available seat
    Then a booking should be created
    And the seat should be marked as booked
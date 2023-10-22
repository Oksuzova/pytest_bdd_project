@e2e
Feature: Book_manager

  Scenario: New book should be add to unread shelf
    Given Create book with <name> name and <author> author
    When <add> current book in to closet
    Then Current book <present> in closet at <unread> shelf
    And Current book is <unreaded>
    And Current book <not_present> in closet at <read> shelf
    And Closet <read> book counter equal <0>
    And Closet <unread> book counter equal <1>

  Scenario: Book should have read status after reading
    Given Create book with <name> name and <author> author
    When <add> current book in to closet
    And Current book is <unreaded>
    And <read> current book in to closet
    Then Current book <present> in closet at <read> shelf
    And Current book <not_present> in closet at <unread> shelf
    And Closet <read> book counter equal <1>
    And Closet <unread> book counter equal <0>

  Scenario: Retrieve a book from read shelf
    Given A book with <name> name and <author> author is added to the <read> shelf
    When <retrieve> current book from closet
    Then Current book <not_present> in closet at <read> shelf
    And Closet <read> book counter equal <0>

  Scenario: Retrieve a book from unread shelf
    Given A book with <name> name and <author> author is added to the <unread> shelf
    When <retrieve> current book from closet
    Then Current book <not_present> in closet at <unread> shelf
    And Closet <unread> book counter equal <0>

  Scenario: Counting unread books
    Given No books are added to the <unread> shelf
    When A book with <name> name and <author> author is added to the <unread> shelf
    Then Closet <unread> book counter equal <1>

  Scenario: Counting read books
    Given No books are added to the <read> shelf
    When A book with <name> name and <author> author is added to the <read> shelf
    Then Closet <read> book counter equal <1>

  Scenario: Counting the total number of books
    Given No books are added to the <unread> shelf
    Given No books are added to the <read> shelf
    When A book with <name> name and <author> author is added to the <read> shelf
    And A book with <name> name and <author> author is added to the <unread> shelf
    Then Closet <total> book counter equal <2>

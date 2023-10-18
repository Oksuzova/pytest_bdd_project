#    def test_retrieve(self):
#        book = Book(name=name, author=author)
#        self.assertEqual(self.closet.retrieve(book.name), None, msg="None wasn`t return")
#        self.closet.read.add(book)
#        self.assertEqual(self.closet.retrieve(book.name), book, msg="Book wasn`t return")
#        self.assertEqual(self.closet.count_unread, 0, msg="Book was returned, but still present in unread shelf")
#        self.closet.no_read.add(book)
#        self.assertEqual(self.closet.retrieve(book.name), book, msg="Book wasn`t return")
#        self.assertEqual(self.closet.count_read, 0, msg="Book was returned, but still present in read shelf")

Feature: Book_manager

  Scenario: New book should be add to unread shelf
    Given Create book with <name> name and <author> author
    When <Add> <current> book in to closet
    #When <Read> <current> book in closet
    #When <Retrieve> <current> book from closet
    Then <current> book <present> in closet at <unread> shelf
    Then <current> book is <unreaded>
    Then <current> book <not_present> in closet at <read> shelf
    Then Closet <read> book counter equal <0>
    Then Closet <unread> book counter equal <1>

  Scenario: Book should have read status after reading
    Given Create book with <name> name and <author> author
    When <Add> <current> book to closet
    When <current> book is <unreaded>
    When <Read> <current> book in closet
    Then <current> book <present> in closet at <read> shelf
    Then <current> book <not_present> in closet at <unread> shelf
    Then Closet <read> book counter equal <1>
    Then Closet <unread> book counter equal <0>



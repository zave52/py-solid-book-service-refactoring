import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class BookDisplayer(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleBookDisplayer(BookDisplayer):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseBookDisplayer(BookDisplayer):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])


class BookPrinter(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book, displayer: BookDisplayer) -> None:
        pass


class ConsoleBookPrinter(BookPrinter):
    @staticmethod
    def print_book(
        book: Book,
        displayer: BookDisplayer = ConsoleBookDisplayer
    ) -> None:
        print(f"Printing the book: {book.title}...")
        displayer.display(book)


class ReverseBookPrinter(BookPrinter):
    @staticmethod
    def print_book(
        book: Book,
        displayer: BookDisplayer = ReverseBookDisplayer
    ) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        displayer.display(book)


class BookSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        pass


class JSONBookSerializer(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def display_book(book: Book, display_type: str) -> None:
    if display_type == "console":
        ConsoleBookDisplayer.display(book)
    elif display_type == "reverse":
        ReverseBookDisplayer.display(book)
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def print_book(book: Book, print_type: str) -> None:
    if print_type == "console":
        ConsoleBookPrinter.print_book(book)
    elif print_type == "reverse":
        ReverseBookPrinter.print_book(book)
    else:
        raise ValueError(f"Unknown print type: {print_type}")


def serialize_book(book: Book, serialize_type: str) -> str:
    if serialize_type == "json":
        return JSONBookSerializer.serialize(book)
    elif serialize_type == "xml":
        return XMLBookSerializer.serialize(book)
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")

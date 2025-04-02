from school_schedule.student import Student


def test_new_valid_student():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = Student(name, grade, classes)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1


def test_add_class():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    new_class = "Writing"

    # Act
    ellis = Student(name, grade, classes)
    ellis.add_class(new_class)

    # Assert
    assert len(ellis.classes) == 2


def test_get_num_classes():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Writing"]
    ellis = Student(name, grade, classes)

    # Act
    num_classes = ellis.get_num_classes()

    # Assert
    assert num_classes == 2


def test_summary_one_class():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = Student(name, grade, classes)

    # Act
    summary = ellis.summary()

    # Assert
    assert summary == "Ellis is a junior " \
        "enrolled in 1 class: " \
        "Painting"


def test_summary_zero_classes():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = []
    ellis = Student(name, grade, classes)

    # Act
    summary = ellis.summary()

    # Assert
    assert summary == "Ellis is a junior " \
        "enrolled in 0 classes: "


def test_summary_more_than_one_class():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Writing"]
    ellis = Student(name, grade, classes)

    # Act
    summary = ellis.summary()

    # Assert
    assert summary == "Ellis is a junior " \
        "enrolled in 2 classes: " \
        "Painting, Writing"

from sqlalchemy.orm import Session

from . import model, schemas, constant


def get_vehicle_by_identifier(db: Session, identifier: int):
    return (
        db.query(model.Vehicle).filter(model.Vehicle.identifier == identifier).first()
    )


def get_vehicle_by_domain(db: Session, domain: str):
    return db.query(model.Vehicle).filter(model.Vehicle.domain == domain).first()


def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_user = model.Vehicle(**vehicle)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_identifier(domain):
    identifier = 1

    domain_split = domain.split("-")

    identifier += sum_letters(domain_split[0])

    identifier += sum_numbers(domain_split[1])

    return identifier


def sum_letters(domain_text):
    number = 0

    # GET THE VALUE OF THE POSITION 4
    #  ↓
    # [AAAA]
    number += constant.LETTERS[domain_text[0]] * constant.POSITION_4

    # GET THE VALUE OF THE POSITION 3
    #   ↓
    # [AAAA]
    number += constant.LETTERS[domain_text[1]] * constant.POSITION_3

    # GET THE VALUE OF THE POSITION 2
    #    ↓
    # [AAAA]
    number += constant.LETTERS[domain_text[2]] * constant.POSITION_2

    # GET THE VALUE OF THE POSITION 1
    #     ↓
    # [AAAA]
    number += constant.LETTERS[domain_text[3]] * constant.POSITION_1

    return number


def sum_numbers(numbers):
    number = 0

    number += int(numbers[0]) * 100

    number += int(numbers[1]) * 10

    number += int(numbers[2])

    return number


def get_domain(identifier):
    response = ""
    identifier -= 1

    # GET THE VALUE OF THE POSITION 4
    #  ↓
    # [AAAA]
    value_of_letter = identifier // constant.POSITION_4
    response += constant.NUMBERS[value_of_letter]
    identifier -= constant.LETTERS[response[0]] * constant.POSITION_4

    # GET THE VALUE OF THE POSITION 3
    #   ↓
    # [AAAA]
    value_of_letter = identifier // constant.POSITION_3
    response += constant.NUMBERS[value_of_letter]
    identifier -= constant.LETTERS[response[1]] * constant.POSITION_3

    # GET THE VALUE OF THE POSITION 2
    #    ↓
    # [AAAA]
    value_of_letter = identifier // constant.POSITION_2
    response += constant.NUMBERS[value_of_letter]
    identifier -= constant.LETTERS[response[2]] * constant.POSITION_2

    # GET THE VALUE OF THE POSITION 1
    #     ↓
    # [AAAA]
    value_of_letter = identifier // constant.POSITION_1
    response += constant.NUMBERS[value_of_letter]
    identifier -= constant.LETTERS[response[3]] * constant.POSITION_1

    numbers = str(identifier % 10)
    identifier //= 10
    numbers += str(identifier % 10)
    identifier //= 10
    numbers += str(identifier % 10)
    response += "-" + numbers[::-1]

    return response

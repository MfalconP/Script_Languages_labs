import logging
import sys
import re


def get_message_type(event_description):
    if re.search(r"Accepted", event_description):
        return "udane logowanie"
    elif re.search(r"Failed password", event_description):
        return "błędne hasło"
    elif re.search(r"Invalid user", event_description):
        return "błędna nazwa użytkownika"
    elif re.search(r"Disconnected", event_description):
        return "zamknięcie połączenia"
    elif re.search(r"Failed", event_description):
        return "nieudane logowanie"
    elif re.search(r"POSSIBLE BREAK-IN ATTEMPT", event_description):
        return "próba włamania"
    else:
        return "inne"


def log(logfile):
    my_logger = logging.getLogger('my_logger')

    # Ustaw poziom logowania na poziomie DEBUG
    my_logger.setLevel(logging.DEBUG)

    # Utwórz handler dla logów poziomu DEBUG i przypisz go do loggera
    debug_handler = logging.StreamHandler(sys.stdout)
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    my_logger.addHandler(debug_handler)

    # Utwórz handler dla logów poziomu INFO i przypisz go do loggera
    info_handler = logging.StreamHandler(sys.stdout)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    my_logger.addHandler(info_handler)

    # Utwórz handler dla logów poziomu WARNING i przypisz go do loggera
    warning_handler = logging.StreamHandler(sys.stdout)
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    my_logger.addHandler(warning_handler)

    # Utwórz handler dla logów poziomu CRITICAL i przypisz go do loggera
    critical_handler = logging.StreamHandler(sys.stdout)
    critical_handler.setLevel(logging.CRITICAL)
    critical_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    my_logger.addHandler(critical_handler)

    # Utwórz handler dla logów poziomu ERROR i przypisz go do loggera
    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    my_logger.addHandler(error_handler)

    with open(logfile, 'r') as file:
        for line in file:
            my_logger.log(logging.DEBUG, 'Liczba przeczytanych bajtów: %d', len(line))

            msg = get_message_type(line)

            if msg == "udane logowanie":
                match = re.search(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b', line)
                if match:
                    my_logger.log(logging.INFO, 'Zalogowano użytkownika: %s', match.group(1))

            if msg == "nieudane logowanie":
                match = re.search(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b', line)
                if match:
                    my_logger.log(logging.WARNING, 'Nieudana próba logowania użytkownika: %s', match.group(1))

            if msg == "błędne hasło":
                my_logger.log(logging.ERROR, 'Błąd: %s', "błędne hasło")
            elif msg == "błędna nazwa użytkownika":
                my_logger.log(logging.ERROR, 'Błąd: %s', "błędna nazwa użytkownika")

            if msg == "próba włamania":
                match = re.search(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b', line)
                if match:
                    my_logger.log(logging.CRITICAL, 'Proba włamania: %s', match.group(1))


if __name__ == '__main__':
    log("SSH_Lite.log")

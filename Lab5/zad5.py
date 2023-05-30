import zad1
import zad3
import zad4
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Log analyzer CLI')
    parser.add_argument('log_file', type=str, help='path to log file')
    parser.add_argument('--min-level', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='minimum log level')

    subparsers = parser.add_subparsers(dest='command')

    ip_parser = subparsers.add_parser("get_ips", help="prints all ip's in log")
    user_parser = subparsers.add_parser("get_users", help="prints all users in log")
    random_parser = subparsers.add_parser("random", help="randoms user and prints his random lines")
    login_parser = subparsers.add_parser("login", help="calculates most and less frequent users")
    logging_parser = subparsers.add_parser("logging", help="enrolls the logger")

    args = parser.parse_args()

    if args.command == 'get_ips':
        log = zad1.read_ssh_logs(args.log_file)
        print(zad1.get_ipv4s_from_log(log))
    elif args.command == 'get_users':
        log = zad1.read_ssh_logs(args.log_file)
        print(zad1.get_user_from_log(log))
    elif args.command == 'random':
        print(zad4.random_logs_for_user(args.log_file))
    elif args.command == 'login':
        least_frequent_users, most_frequent_users = zad4.calculate_login_frequency(args.log_file)
        print(f'Least frequent logins: {least_frequent_users}')
        print(f'Most frequent logins: {most_frequent_users}')
    elif args.command == 'logging':
        zad3.log(args.log_file)

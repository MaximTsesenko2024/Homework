from time import sleep


class Users:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password_hash = hash(password)
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Users):
            return self.nickname == other.nickname
        elif isinstance(other, str):
            return self.nickname == other
        elif other is None:
            return False
        else:
            print('Неправильный тип данных.')
            return None

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.nickname

    def __lt__(self, other):
        if isinstance(other, int):
            return self.age < other
        else:
            print('Неправильный тип данных.')
            return None


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        elif isinstance(other, str):
            return other.lower() in self.title.lower()
        elif other is None:
            return False
        else:
            print('Неправильный тип данных.')
            return None

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def find_user(self, nickname: str):
        for i in self.users:
            if i == nickname:
                return i
        return None

    def register(self, nickname, password, age):
        if self.find_user(nickname) is None:
            user = Users(nickname, password, int(age))
            self.users.append(user)
            self.current_user = user
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):
        user = self.find_user(nickname)
        if isinstance(user, Users):
            if user.password_hash == hash(password):
                self.current_user = user
            else:
                print("Неверный пароль.")
        else:
            print(f"Пользователя {nickname} не существует. Выполните регистрацию")

    def log_out(self):
        self.current_user = None

    def __del__(self):
        self.log_out()

    def add(self, *args):
        for i in args:
            find = False
            for j in self.videos:
                if j == i:
                    find = True
            if not find:
                self.videos.append(i)

    def get_videos(self, name):
        find = []
        for i in self.videos:
            if i == name:
                find.append(str(i))
        return find

    def watch_video(self, name_film):
        def find_video(videos, name):
            for i in videos:
                if i.title == name:
                    return i
            return None

        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return 1
        found_video = find_video(self.videos, name_film)
        if isinstance(found_video, Video):
            if found_video.adult_mode:
                if self.current_user < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return 2

            print(f'Воспроизведение видео "{found_video}"')
            for i in range(found_video.time_now + 1, found_video.duration + 1):
                print(i, end=' ')
                sleep(1)
            print('Конец видео', end='\n')
            return 0
        else:
            print(f'Видео "{name_film}" не найдено.')
            return 3


if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    while True:
        choice = input('Выберите действие\n1 - Регистрация нового пользователя\n'
                           '2 - Вход пользователя\n'
                           '3 - Добавить видео\n4 - Найти видео\n5 - Просмотр видео\n0 - Выход\n')
        if not choice in '012345':
            print('Неравильный ввод. Повторите')
            continue
        else:
            choice = int(choice)
        if choice == 1:
            login = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            age = input('Введите возраст: ')
            ur.register(login, password, age)
        elif choice == 2:
            login = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            ur.log_in(login, password)
        elif choice == 3:
            title = input('Введите название фильма: ')
            duration = input('Введите продолжительность фильма в секундах: ')
            adult_mode = input('Возрастное ограничение Да(Y)/нет(N): ')
            video = Video(title, int(duration), adult_mode=(adult_mode == 'Y'))
            ur.add(video)
            print('Видео добавлено')
        elif choice == 4:
            name = input('Введите название видео или его часть: ')
            videos = ur.get_videos(name)
            if len(videos) == 0:
                print('Видео не найдено.')
            else:
                print(videos)
        elif choice == 5:
            name = input('Введите название видео: ')
            ur.watch_video(name)
        elif choice == 0:
            print('Выход из программы.')
            exit()

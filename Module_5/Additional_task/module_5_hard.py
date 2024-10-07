class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def find_user_by_name(self, name):
        for user in self.users:
            if user.nickname == name:
                return user
        return None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return f"Пользователь {nickname} вошел в систему."
        return "Неверный логин или пароль."

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users.append(User(nickname, password, age))
        self.current_user = nickname
        print(f'Пользователь {nickname} успешно зарегестрирован!')

    def add(self, *args):
        for item in args:
            if not any(item.title == video.title for video in self.videos):
                self.videos.append(item)

    def get_videos(self, search_word):
        results = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                results.append(video.title)
        return results if results else None

    def watch_video(self, title_name):
        if self.current_user is None:
            print('Вы должны войти в систему, чтобы смотреть видео!')
            return

        for video in self.videos:
            if title_name == video.title:
                if video.adult_mode and self.find_user_by_name(self.current_user).age < 18:
                    print('Вам нет 18 лет!!! Покиньте страницу быстра!!!')
                    return
                loading_bar(video.duration)
                video.duration = 0
                return


def loading_bar(total=None, length=20):
    from time import sleep
    for i in range(total + 1):
        filled_length = int(length * i // total)
        bar = '█' * filled_length + '-' * (length - filled_length)
        print(f'\r|{bar}| {i}/{total} ({(i / total) * 100:.2f}%)', end='')
        sleep(0.3)
    print(' Конец видео!')


if __name__ == '__main__':
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







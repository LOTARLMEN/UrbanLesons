class UrTube:
    users = []
    videos = []


    def __init__(self):
        self.current_user = None
        self.password = None
        self.age = None
        self.nickname = None

    def log_in(self, nickname, password):
        for item in self.users:
            if nickname == item['Nickname'] and hash(password) == item['Password']:
                UrTube.current_user = nickname
                print(f'Пользователь успешно залогинился!\n'
                      f'Текущий пользователь: {self.current_user}.')
            else:
                if int(input('Такого пользователя не существует.\n'
                         'Хотите зарегистрироваться?\n'
                         'Введите 1 для регистрации или 2 для окончания программы: ')) == 1:
                    return self.register()
                else:
                    break


    def register(self, nickname=None, password=None, age=None):
        self.nickname = input('Введите ник для регистрации: ')
        for item in UrTube.users:
            if self.nickname in item['Nickname']:
                print('Такой ник уже есть у другого пользователя.')
                if int(input('Если вы хотите зарегистрироваться введите 1, либо Enter, если передумали: ')) == 1:
                    return self.register()
                else: return None
        self.password = input('Введите пароль: ')
        while True:
            try:
                self.age = int(input('Введите ваш возсраст: '))
                if isinstance(self.age, int) == False or self.age <= 0:
                    print(f'Как вам может быть {self.age}?')
                    continue
                elif self.age < 6:
                    print('А вы не слишком маловаты для подобных вещей?')
                    continue
                break
            except ValueError:
                print('Вы ввели не целое число!')
        self.users.append({'Nickname': self.nickname, 'Password': hash(self.password), 'Age': int(self.age)})
        self.current_user = self.nickname
        print(f'Пользователь с никнеймом: {self.nickname} успешно зарегистрирован.')

    def __add__(self, other):
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if not any(v['title'] == video.title for v in self.videos):
                self.videos.append({
                    'title': video.title,
                    'duration': video.duration,
                    'time_now': video.time_now,
                    'adult_mode': video.adult_mode
                })

    def get_videos(self, search_word):
        return [video['title'] for video in self.videos if search_word.lower() in video['title'].lower()]


    def watch_video(self, name_title):
        if self.current_user is None:
            print('Вы должны войти в систему, чтобы смотреть видео!')
            return

        for video in self.videos:
            if video['title'] == name_title:
                if video['adult_mode'] and self.age < 18:
                    print('Название ролика не верно, либо вам нет 18 лет, чтобы смотреть данный ролик!')
                    return
                return loading_bar(video["duration"])

        print('Название ролика не верно, либо вам нет 18 лет, чтобы смотреть данный ролик!')


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = adult_mode
        UrTube.videos.append({'title': self.title,
                              'duration': self.duration,
                              'time_now': self.time_now,
                              "adult_mode": self.adult_mode})

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        UrTube.users.append({'Nickname': self.nickname, 'Password': hash(self.password), 'Age': self.age})

def loading_bar(total=None, length=20):
    from time import sleep
    for i in range(total + 1):
        filled_length = int(length * i // total)
        bar = '█' * filled_length + '-' * (length - filled_length)
        print(f'\r|{bar}| {i}/{total} ({(i / total) * 100:.2f}%)', end='')
        sleep(0.2)
    print('Конец видео!')

if __name__ == '__main__':
    # b = UrTube()
    # a = User('Kaka', 123, 13)
    #  print(UrTube.current_user)
    #  print(UrTube.users)
    #  b.register()
    #  print(UrTube.users)
    # b.log_in('Kaka', 123)

    # print(UrTube.users)

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

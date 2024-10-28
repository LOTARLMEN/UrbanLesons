import unittest
from runner_and_tournament import Tournament, Runner


class TournamentTest(unittest.TestCase):
    DISTANCE_TOURNAMENT = 90
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def setUp(self):
        self.first_runner = Runner('Усэйн', speed=10)
        self.second_runner = Runner('Андрей', speed=9)
        self.third_runner = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in TournamentTest.all_results:
            formatted_result = {place: runner.name for place, runner in result.items()}
            print(formatted_result)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_start_tournament(self):
        self.tournament = Tournament(self.DISTANCE_TOURNAMENT, self.first_runner, self.third_runner)
        self.result = self.tournament.start()
        TournamentTest.all_results.append(self.result)
        self.assertEqual(self.result[max(self.result.keys())].name, self.third_runner.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_start_tournament_2(self):
        self.tournament = Tournament(self.DISTANCE_TOURNAMENT, self.second_runner, self.third_runner)
        self.result = self.tournament.start()
        TournamentTest.all_results.append(self.result)
        self.assertEqual(self.result[max(self.result.keys())].name, self.third_runner.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_start_tournament_3(self):
        self.tournament = Tournament(self.DISTANCE_TOURNAMENT, self.first_runner, self.second_runner, self.third_runner)
        self.result = self.tournament.start()
        TournamentTest.all_results.append(self.result)
        self.assertEqual(self.result[max(self.result.keys())].name, self.third_runner.name)


if __name__ == '__main__':
    unittest.main()
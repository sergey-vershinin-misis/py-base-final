from unittest import TestCase

from task01.task_manager import TaskManager


class TestTaskManager(TestCase):

    def test_task_manager_initialization(self):
        manager = TaskManager()

        self.assertEqual(manager.task_count(), 0, "Количество задач после создания менеджера отлично от 0")

    def test_task_manager_add_task(self):
        manager = TaskManager()
        manager.add_task("name 1", 1)

        self.assertEqual(manager.task_count(), 1, 'Количество задач после добавления не совпадает с ожидаемым')
        self.assertTrue(manager.contains_task("name 1"), 'Менеджер не содержит только что добавленную задачу')

    def test_task_manager_raise_error_when_adding_duplicate_task(self):
        manager = TaskManager()
        manager.add_task("name 1", 1)

        with self.assertRaises(ValueError):
            manager.add_task("name 1", 2)

    def test_task_manager_remove_task(self):
        manager = TaskManager()
        manager.add_task("name 1", 1)
        manager.add_task("name 2", 2)
        manager.remove_task("name 1")

        self.assertFalse(manager.contains_task("name 1"), "После удаления задача осталась в менеджере")
        self.assertEqual(manager.task_count(), 1, "Количество задач после удаления не совпадает с ожидаемым")

    def test_task_manager_contains_task(self):
        manager = TaskManager()
        manager.add_task("name 1", 1)
        manager.add_task("name 2", 2)

        self.assertTrue(manager.contains_task("name 1"), "Менеджер не находит добавленную задачу")
        self.assertFalse(manager.contains_task("name 3"), "Менеджер находит задачу, которую ранее не добавляли")

    def test_task_manager_output(self):
        manager = TaskManager()
        manager.add_task("n1", 2)
        manager.add_task("n2", 2)
        manager.add_task("n3", 1)
        manager.add_task("n4", 3)

        self.assertEqual(manager.__repr__(), "1 n3\n2 n1, n2\n3 n4",
                         'Текстовое представление менеджера не совпадает с ожидаемым')

# from aiogram.fsm.state import StatesGroup, State
#
#
# class GetCountMembers(StatesGroup):
#     """Создайте состояние, чтобы получить количество членов группы"""
#     get_count_members_grup = State()
#
#
# class AddUserStates(StatesGroup):
#     WAITING_FOR_USER_ID = State()  # ожидание ввода ID пользователя;
#     USER_ADDED = State()  # состояние, когда пользователь успешно добавлен в базу данных.
#
#
# class AddAndDelBadWords(StatesGroup):
#     """Создаем состояние для добавления плохих слов"""
#     waiting_for_bad_word = State()
#     waiting_for_check_word = State()
#     del_for_bad_word = State()

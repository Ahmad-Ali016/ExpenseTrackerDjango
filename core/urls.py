from django.urls import include, path
from core.views import index_view, list_expenses_view, add_expense_view, edit_expense, delete_expense
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("index/", index_view, name="index_view"),
    path('list-expenses/', list_expenses_view, name='list_expenses'),
    path('expenses/add/', add_expense_view, name='add_expense'),
    path('edit-expense/<int:expense_id>', edit_expense, name='edit_expense'),
    path('delete-expense/<int:expense_id>', delete_expense, name='delete_expense'),

    # # Hotel URLs
    # path("list-hotels/", list_hotels_view, name="list_hotels_view"),
    # path('add-hotel', add_hotel, name='add_hotel'),
    # path('edit-hotel/<int:hotel_id>', edit_hotel, name='edit_hotel'),
    # path('delete-hotel/<int:hotel_id>', delete_hotel, name='delete_hotel'),
    #
    #
    # # Room Types URL's
    # # path("list-room-types/", list_room_types, name="list_room_types"),
    # path("hotel/<int:hotel_id>/room-types/", list_room_types, name="list_room_types"),
    # path('hotel/<int:hotel_id>/room-types/<int:room_type_id>/rooms/', list_rooms_by_room_type, name='list_rooms_by_room_type'),
    # path('test-ui', test_ui, name='test_ui'),
]

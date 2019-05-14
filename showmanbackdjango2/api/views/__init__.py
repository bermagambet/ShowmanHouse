from .generic_cbv import AttendeesList, AttendeesDetail, EventTypesList, OrdersList, ShowmanHouseList,\
    UserViewSet, CountryList, CityList, AddressDetail, DiscountList, PaymentList, FeeList, EmployeesList,\
    AvatarList, EventAvatarList, OurEventsList, OurEventsList2
from .auth import UserList, login, logout, current_user

# from .image import upload_pic

from .attendees import attendee_detail, eventtype_detail, orders_detail,\
    showmanhouse_detail, adress_detail, city_detail, country_detail, discount_detail, fee_detail,\
    payment_detail, employee_detail, avatar_detail, eventavatar_detail, ourevent_detail
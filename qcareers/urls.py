from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='qcareers-home'),
    path('search_job/', views.searchJob, name='qcareers-search-job'),
    path('job_recommendation/', views.recommendJob, name='qcareers-recommend-job'),
    path('recommended_job/', views.recommendedJob, name='qcareers-recommended-job'),
    path('manage_skills/', views.manageSkills, name='qcareers-manage-skills'),
    path('manage_modules/', views.manageModules, name='qcareers-manage-modules'),
    path('manage_jobs/', views.manageJobs, name='qcareers-manage-jobs'),
    path('my_recommendations/', views.myRecommendations, name='qcareers-my-recommendations'),
    path('request_admin/', views.requestAdmin, name='qcareers-request-admin'),
    path('manage_requests/', views.manageRequestsGet, name='qcareers-manage-requests-get'),
    url(r'^manage_requests/(?P<admReqId>\d+)/$', views.manageRequestsPost, name='qcareers-manage-requests-post'),
    path('ajax/', views.ajax, name='ajax'),
    path('data/', views.ajaxData, name='ajaxData'),

    path('support_page/', views.supportPage, name='qcareers-support-page'),
    path('support_chat/', views.supportChat, name='qcareers-support-chat'),
    url(r'^get_messages/$', views.getMessages, name='qcareers-get-messages'),

    path('support_page_for_admins/', views.supportPageForAdmins, name='qcareers-support-page-for-admins'),
    url(r'^support_chat_for_admins/(?P<userId>\d+)/$', views.supportChatForAdmins, name='qcareers-support-chat-for-admins'),
    url(r'^get_messages_for_admins/$', views.getMessagesForAdmins, name='qcareers-get-messages-for-admins'),

    url(r'^post_message/$', views.postMessage, name='qcareers-post-message'),
    url(r'^post_message_for_admins/$', views.postMessageForAdmins, name='qcareers-post-message-for-admins'),
    url(r'^delete_chat/(?P<username>[\w\-]+)/$', views.deleteChat, name='qcareers-delete-chat'),

    path('check_for_notifs/', views.checkForNotifs, name='check_for_notifs/'),

    path('test/', views.test, name='test'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('upload/trackone/',views.upload_trackone,name='upload-trackone'),
    path('upload/tracktwo/',views.upload_tracktwo,name='upload-tracktwo'),
    path('upload/trackone/edit/',views.upload_trackone_edit,name='upload-trackone-edit'),
    path('upload/tracktwo/edit/',views.upload_tracktwo_edit,name='upload-tracktwo-edit'),
    path('upload/finalized/track/',views.finalize_track_edit,name='finalize-track-edit'),
]


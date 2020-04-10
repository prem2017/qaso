from django.urls import path
from . import views


urlpatterns = [
    path('', views.questions, name='home-page'), # '' => indicates that <views.questions> will be called on home page of the app.
    path('qac', views.qac, name='async-qac'),
]



# from django.conf.urls import url

# from . import views
# from . import templatePredictorView

# urlpatterns = [

# 	url(r'^$', views.index, name='index_o'),
# 	url(r'^tp$', templatePredictorView.index, name='index'),

# 	url(r'^pre_process_text$', templatePredictorView.pre_process_text, name='pre_process_text'),
# 	url(r'^predict_answering_template$', templatePredictorView.predict_answering_template, name='predict_answering_template'),
# 	url(r'^predict_answering_template_for_chronological_text$', templatePredictorView.predict_answering_template_for_chronological_text, name='predict_answering_template_for_chronological_text'),
# 	url(r'^predict_answering_template_group$', templatePredictorView.predict_answering_template_group, name='predict_answering_template_group'),
# 	url(r'^update_training_data$', templatePredictorView.update_training_data, name='update_training_data'),
# 	url(r'^predict_sentiment$', templatePredictorView.predict_sentiment, name='predict_sentiment'),
# 	url(r'^retrain_calssifier_models$', templatePredictorView.retrain_calssifier_models, name='retrain_calssifier_models'),
# 	url(r'^get_processed_module_test_report', templatePredictorView.get_processed_module_test_report, name='get_processed_module_report$'),

# ]

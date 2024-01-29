from django.urls import path
from . import views

urlpatterns = [
    path("branch-test", views.branch_test, name="branchTest"),
    path("area-test-ayt", views.area_test_ayt, name="areaTestAyt"),
    path("area-test-tyt", views.area_test_tyt, name="areaTestTyt"),
    path(
        "branch-test/filter-test-branch",
        views.filter_test_branch,
        name="filterTestBranch",
    ),
    path("calc-score", views.calc_score, name="calcScore"),
]

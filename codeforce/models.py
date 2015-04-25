from django.db import models

# Create your models here.

class CFUsers(models.Model):
    user_name = models.CharField(max_length = 100)
    user_email = models.EmailField()
    user_gender = models.CharField(max_length=1, default='M')
    user_location = models.CharField(max_length=100)
    user_points = models.IntegerField()
    user_contest_num = models.IntegerField()

class friends(models.Model):
    uid = models.IntegerField()
    fid = models.IntegerField()

class Problem(models.Model):
    problem_title = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    solved_num = models.IntegerField()
    difficulty_type = models.IntegerField()
    description = models.CharField(max_length=500)
    answer = models.CharField(max_length=100)
    trial_num = models.IntegerField()

class Contest(models.Model):
    contest_name = models.CharField(max_length = 200)
    contest_creater = models.CharField(max_length=100)
    contest_duration = models.IntegerField()
    contest_start_time = models.DateTimeField()
    contest_end_time = models.DateTimeField()
    contest_description = models.CharField(max_length=500)
    contest_participant_num = models.IntegerField()
    contest_total_points = models.IntegerField(default = 100)

class ContestProblems(models.Model):
    contest = models.ForeignKey(Contest)
    contest_problem = models.ForeignKey(Problem)
    cp_points = models.IntegerField()
    cp_trial_num = models.IntegerField()
    cp_success_num = models.IntegerField()


# class ContestProblemList(models.Model):
#     """the list of problems if a contest"""
#     # cpl_cid = models.IntegerField()
#     # contest = models.ForeignKey(Contest)
#     cpl_problem = models.ForeignKey(Problem)
#     cpl_trial_num = models.IntegerField()
#     cpl_success_num = models.IntegerField()

class ContestParticipantInfo(models.Model):
    # ci_cid = models.IntegerField()
    # ci_pid = models.IntegerField()
    # ci_uid = models.IntegerField()
    # ci_is_right = models.BooleanField()
    # ci_trial_date = models.TimeField()
    # ci_trial_answer = models.IntegerField()
    cpi_contest = models.ForeignKey(Contest)
    cpi_user = models.ForeignKey(CFUsers)
    cpi_problem = models.ForeignKey(Problem)
    cpi_is_right = models.BooleanField()
    cpi_trial_time = models.DateTimeField()
    cpi_trial_answer = models.IntegerField()

class ContestResults(models.Model):
    # cr_cid = models.IntegerField()
    # cr_uid = models.IntegerField()
    # cr_points = models.IntegerField()
    cr_contest = models.ForeignKey(Contest)
    cr_user = models.ForeignKey(CFUsers)
    cr_points = models.IntegerField()
    cr_is_submited = models.BooleanField(default=False)

class OngoingContest(models.Model):
    oc_contest = models.ForeignKey(Contest)
    oc_user = models.ForeignKey(CFUsers)
    oc_start_time = models.DateTimeField()
    oc_end_time = models.DateTimeField()
    oc_points = models.IntegerField()
    oc_is_simulation = models.BooleanField(default=False)
    oc_is_finished = models.BooleanField(default=False)


        







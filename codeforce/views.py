#!/usr/bin/env python
"""
Author:     Zhikai Ding
For:        CS5200 Project CodeForce
version:    "1.0"
"""

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.db import connection
from codeforce.models import *
from django.db.models.functions import Lower
from django.utils import timezone
import datetime
import re, sys
import hashlib
import urllib2


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

"""view functions"""
def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('codeforce:home'))

    invalid_pwd = False
    if len(request.POST) == 0:
        return render(request, 'codeforce/index.html', {'the_user': request.user.username, 'invalid_pwd': invalid_pwd})

    un = request.POST['username']
    pwd = request.POST['pwd']

    user = authenticate(username = un, password = pwd)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('codeforce:home'))
        else:
            pass
    else:
        invalid_pwd = True

    return render(request, 'codeforce/index.html', {'the_user': request.user.username, 'invalid_pwd': invalid_pwd})


def signup(request):
    if len(request.POST) == 0:
        return render(request, 'codeforce/signup.html', {'the_user': request.user.username, 'reg_fail': False})

    username = request.POST['username']
    pwd = request.POST['pwd']
    email = request.POST['email']
    gender = request.POST['gender']
    loc = request.POST['location']
    try:
        user = User.objects.create_user(username, email, pwd)
        user.save()
        cfu = CFUsers(
            id = user.id, 
            user_name = username, 
            user_email = email, 
            user_points = 0,
            user_contest_num = 0,
            user_location = loc)
        cfu.save()
        # c = connection.cursor()
        # c.execute("insert into users(uname, email, gender, location, pwd)"
        #           "values(%s, %s, %s, %s, %s)", [username, email, gender, loc, pwd])
    except:
        e = sys.exc_info()[0]
        print e
        return render(request, 'codeforce/signup.html', {'the_user': request.user.username, 'reg_fail': True})

    return HttpResponseRedirect(reverse('codeforce:home'))

@login_required(login_url = "codeforce:index")
def home(request):
    problems = Problem.objects.filter(difficulty_type = 0)

    return render(request, 'codeforce/home.html', 
        {
            'the_user': request.user.username,
            'problems':problems 
        })


@login_required(login_url = "codeforce:index")
def home_medium(request):
    problems = Problem.objects.filter(difficulty_type = 1)

    return render(request, 'codeforce/home.html', {'the_user': request.user.username,
                                                  'is_medium': True, 'problems':problems })


@login_required(login_url = "codeforce:index")
def home_hard(request):
    problems = Problem.objects.filter(difficulty_type = 2)
    return render(request, 'codeforce/home.html', {'the_user': request.user.username,
                                                  'is_hard': True, 'problems':problems })

@login_required(login_url = "codeforce:index")
def problem_detail(request, pid):
    problem = Problem.objects.filter(id = pid)[0]
    print problem.problem_title
    return render(request, 'codeforce/problem.html', 
        {'the_user':request.user.username,
        'problem':problem})

@login_required(login_url = "codeforce:index")
def problem_check(request, pid):
    problem = Problem.objects.filter(id = pid)[0]
    if problem:
        problem.trial_num += 1
        if problem.answer == request.POST['guess_36']:
            problem.solved_num += 1
            problem.save()
            return render(request, 'codeforce/problem_check.html', 
                {'the_user':request.user.username,
                'problem':problem,
                'successful':True})
        else:
            problem.save()
            return render(request, 'codeforce/problem_check.html', 
                {'the_user':request.user.username,
                'problem':problem,
                'successful':False})

@login_required(login_url = "codeforce:index")
def check_ongoing(request, cid, ocid, pid):
    answer = request.POST['guess_36']
    problem = Problem.objects.filter(id = pid)[0]
    contest = Contest.objects.filter(id=cid)[0]
    user = CFUsers.objects.filter(id=request.user.id)[0]
    oc = OngoingContest.objects.filter(id = ocid)[0]
    cps = ContestProblems.objects.filter(contest = oc.oc_contest, contest_problem = pid)[0]
    cpi_right = ContestParticipantInfo.objects.filter(
        cpi_contest=cid, cpi_user=request.user.id, cpi_problem=pid, cpi_is_right=True)
    print cpi_right.count()
    cpi = ContestParticipantInfo(
        cpi_contest=contest,
        cpi_user=user,
        cpi_problem=problem,
        cpi_trial_time=timezone.now(),
        cpi_trial_answer=answer,
        cpi_is_right=False
        )
    cps.cp_trial_num += 1
    if cps is not None and problem is not None:
        problem.trial_num += 1
        cps.cp_trial_num += 1
        if problem.answer == answer:
            cpi.cpi_is_right = True
            problem.solved_num += 1
            cps.cp_success_num += 1
            if cpi_right.count() == 0:
                oc.oc_points += cps.cp_points
            cpi.save()
            oc.save()
            cps.save()
            problem.save()
            return render(request, 'codeforce/problem_check.html', 
                {'the_user':request.user.username,
                'ongoing_contest': oc,
                'problem':problem,
                'successful':True})
        else:
            cpi.save()
            problem.save()
            oc.save()
            cps.save()
            return render(request, 'codeforce/problem_check.html', 
                {'the_user':request.user.username,
                'ongoing_contest': oc,
                'problem':problem,
                'successful':False})

@login_required(login_url = "codeforce:index")
def contest_problem_check(request, cid, pid):
    answer = request.POST['guess_36']
    problem = Problem.objects.filter(id = pid)[0]
    contest = Contest.objects.filter(id=cid)[0]
    if contest is not None and problem is not None:
        problem.trial_num += 1
        if problem.answer == answer:
            problem.solved_num += 1
            problem.save()
            return render(request, 'codeforce/problem_check.html', 
                {'the_user':request.user.username,
                'contest': contest,
                'problem':problem,
                'successful':True})
        else:
            cpi.save()
            problem.save()
            return render(request, 'codeforce/problem_check.html', 
                {'the_user':request.user.username,
                'contest': contest,
                'problem':problem,
                'successful':False})

@login_required(login_url = "codeforce:index")
def contest(request):
    contests = Contest.objects.filter(contest_start_time__lt=datetime.datetime.now())
    for c in contests:
        print c.contest_description
    return render(request, 'codeforce/contest.html', 
        {
            'the_user': request.user.username,
            'contests': contests,
            'is_finished': True,
        })


@login_required(login_url = "codeforce:index")
def contest_detail_default(request, cid):
    cpl = ContestProblems.objects.filter(contest_id = cid)
    contest = Contest.objects.filter(id = cid)[0]
    print contest.id
    print 'default',
    print cid
    problems = []
    for p in cpl:
        problems.append(Problem.objects.filter(id = p.contest_problem_id)[0])
    print len(problems)
    now = timezone.now()
    is_finished = False
    if now > contest.contest_end_time:
        is_finished = True

    return render(request, 'codeforce/contest_detail.html',
        {
            'the_user': request.user.username,
            'problems': problems,
            'contest': contest,
            'cid': cid,
            'cpid': problems[0].id,
            'pnum': len(problems),
            'is_finished': is_finished,
            'range': range(len(problems)),
        })


@login_required(login_url = "codeforce:index")
def contest_detail(request, cid, cpid):
    cpl = ContestProblems.objects.filter(contest_id = cid)
    print cid
    problems = []
    contest = Contest.objects.filter(id = cid)[0]
    for p in cpl:
        problems.append(Problem.objects.filter(id = p.contest_problem_id)[0])
    print len(problems)
    now = timezone.now()
    is_finished = False
    if now > contest.contest_end_time:
        is_finished = True
    return render(request, 'codeforce/contest_detail.html',
        {
            'the_user': request.user.username,
            'problems': problems,
            'cid': cid,
            'contest': contest,
            'cpid': problems[int(cpid)].id,
            'pnum': len(problems),
            'is_finished': is_finished,
            'range': range(len(problems)),
        })


@login_required(login_url = 'codeforce:index')
def rating(request):
    users = CFUsers.objects.all().order_by('-user_points')
    return render(request, 'codeforce/rating.html',
        {
            'the_user': request.user.username,
            'users': users,
        })

@login_required(login_url = 'codeforce:index')
def rating_test(request):
    users = CFUsers.objects.all().order_by('-user_points')
    return render(request, 'codeforce/rating_test.html',
        {
            'the_user': request.user.username,
            'users': users,
        })

def minutes_between(d1, d2):
    year = d2.year - d1.year
    month = d2.month - d1.month
    day = d2.day - d1.day
    hour = d2.hour - d1.hour
    minute = d2.minute - d1.minute
    return day*60*24 + hour * 60 + minute

@login_required(login_url = 'codeforce:idnex')
def current_contest(request):
    now = datetime.datetime.now()
    coming_contests = Contest.objects.filter(contest_start_time__gt=now).order_by('id')
    ongoing_contest = Contest.objects.filter(contest_start_time__lte=now, contest_end_time__gte=now).order_by('id')
    og_crs = []
    for i, c in enumerate(ongoing_contest):
        if ContestResults.objects.filter(cr_contest=c.id, cr_user=request.user.id).count()==0:
            og_crs.append(c.id)
        else:
            og_crs.append(False)
    coming_crs = []
    for i, c in enumerate(coming_contests):
        if ContestResults.objects.filter(cr_contest=c.id, cr_user=request.user.id).count()==0:
            coming_crs.append(c.id)
        else:
            coming_crs.append(False)
    ongoing_left = []
    coming_left = []
    now = datetime.datetime.now()
    for c in coming_contests:
        time = minutes_between(now, c.contest_start_time)
        coming_left.append(time)
    for c in ongoing_contest:
        time = minutes_between(now, c.contest_end_time)
        ongoing_left.append(time)
    return render(request, 'codeforce/current_contest.html',
        {
            'the_user': request.user.username,
            'coming_contests': coming_contests,
            'ongoing_contest': ongoing_contest,
            'ongoing_left': ongoing_left,
            'coming_left': coming_left,
            'coming_crs': coming_crs,
            'og_crs':og_crs
        })


@login_required(login_url = "codeforce:index")
def home_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('codeforce:index'))

def get_end_time(duration):
    # duration = int(duration)
    # start = timezone.now()
    # minutes = start.minute + duration
    # hours = start.hour + int(minutes/60)
    # minutes = minutes % 60
    end_time = datetime.datetime.now() + datetime.timedelta(minutes=duration)
    return end_time

@login_required(login_url = "codeforce:index")
def contest_simulate(request, cid):
    cpl = ContestProblems.objects.filter(contest_id = cid)
    contest = Contest.objects.filter(id = cid)[0]
    print request.user.id
    user = CFUsers.objects.filter(id = request.user.id)[0]
    problems = []
    for p in cpl:
        problems.append(Problem.objects.filter(id = p.contest_problem_id)[0])
    now = timezone.now()
    print 'timezone',
    print now,
    print 'datetime',
    print datetime.datetime.now()
    is_finished = False
    if now > contest.contest_end_time:
        is_finished = True
    end_time = get_end_time(contest.contest_duration)
    print end_time
    oc = OngoingContest(
        oc_contest = contest,
        oc_user = user,
        oc_start_time = timezone.now(),
        oc_end_time = end_time,
        oc_points = 0,
        oc_is_simulation=True
        )
    oc.save()
    return render(request, 'codeforce/contest_simulating.html',
        {
            'the_user': request.user.username,
            'problems': problems,
            'contest': contest,
            'cid': cid,
            'cpid': problems[0].id,
            'pnum': len(problems),
            'ongoing_contest': oc,
            'is_simulating': True,
            # 'end_time': end_time,
            'is_finished': is_finished,
            'range': range(len(problems)),
        })


@login_required(login_url = "codeforce:index")
def real_contest(request, cid):
    cpl = ContestProblems.objects.filter(contest_id = cid)
    if cpl.count()==0:
        return HttpResponseRedirect(reverse('codeforce:home'))
    contest = cpl[0].contest
    print contest.id,
    print contest.contest_end_time
    print request.user.id
    user = CFUsers.objects.filter(id = request.user.id)[0]
    problems = []
    for p in cpl:
        problems.append(Problem.objects.filter(id = p.contest_problem_id)[0])
    now = timezone.now()
    print 'now',
    print now
    print 'datetime',
    print datetime.datetime.now()
    is_finished = False
    if now > contest.contest_end_time:
        is_finished = True
    end_time = contest.contest_end_time
    print end_time
    oc = OngoingContest.objects.filter(oc_contest=cid, oc_user=request.user.id)
    if oc.count() == 0:
        print 'creating'
        oc = OngoingContest(
            oc_contest = contest,
            oc_user = user,
            oc_start_time = now,
            oc_end_time = end_time,
            oc_points = 0,
            oc_is_simulation=False
            )
        print oc.oc_start_time
        oc.save()
    else:
        oc = oc[0]
    print 'oc_end_time',
    print oc.oc_end_time
    return render(request, 'codeforce/contest_simulating.html',
        {
            'the_user': request.user.username,
            'problems': problems,
            'contest': contest,
            'cid': cid,
            'cpid': problems[0].id,
            'pnum': len(problems),
            'ongoing_contest': oc,
            'is_simulating': True,
            # 'end_time': end_time,
            'is_finished': is_finished,
            'range': range(len(problems)),
        })


@login_required(login_url = "codeforce:index")
def ongoing(request, cid, ocid, cpid):
    cpl = ContestProblems.objects.filter(contest_id = cid)
    contest = Contest.objects.filter(id = cid)[0]
    user = CFUsers.objects.filter(id = request.user.id)[0]
    problems = []
    for p in cpl:
        problems.append(Problem.objects.filter(id = p.contest_problem_id)[0])
    is_finished = False
    oc = OngoingContest.objects.filter(id=ocid)[0]
    return render(request, 'codeforce/contest_simulating.html',
        {
            'the_user': request.user.username,
            'problems': problems,
            'contest': contest,
            'cid': cid,
            'cpid': problems[int(cpid)].id,
            'pnum': len(problems),
            'ongoing_contest': oc,
            'is_simulating': True,
            'range': range(len(problems)),
        })


@login_required(login_url = "codeforce:index")
def register(request, cid):
    contests = Contest.objects.filter(contest_start_time__gt=datetime.datetime.now())
    user = CFUsers.objects.filter(id=request.user.id)[0]
    contest = Contest.objects.filter(id=cid)[0]
    cr = ContestResults.objects.filter(cr_contest=cid, cr_user=request.user.id)
    if cr.count() == 0:
        cr=ContestResults(
            cr_contest = contest,
            cr_user = user,
            cr_points = 0
            )
        cr.save()
        contest.contest_participant_num += 1
        contest.save()
    # crs = []
    # for i, c in enumerate(contests):
    #     if ContestResults.objects.filter(cr_contest=c.id, cr_user=request.user.id).count()==0:
    #         print 'found'
    #         crs.append(c.id)
    #     else:
    #         crs.append(False)
    # print crs
    # left_days = []
    # now = datetime.datetime.now()
    # for c in contests:
    #     time = minutes_between(now, c.contest_start_time)
    #     left_days.append(time)

    # return render(request, 'codeforce/current_contest.html',
    #     {
    #         'the_user': request.user.username,
    #         'is_reg_successful': True,
    #         'contests': contests,
    #         'crs': crs,
    #         'left_days': left_days,
    #     })
    now = datetime.datetime.now()
    coming_contests = Contest.objects.filter(contest_start_time__gt=now).order_by('id')
    ongoing_contest = Contest.objects.filter(contest_start_time__lte=now, contest_end_time__gte=now).order_by('id')
    og_crs = []
    for i, c in enumerate(ongoing_contest):
        if ContestResults.objects.filter(cr_contest=c.id, cr_user=request.user.id).count()==0:
            og_crs.append(c.id)
        else:
            og_crs.append(False)
    coming_crs = []
    for i, c in enumerate(coming_contests):
        if ContestResults.objects.filter(cr_contest=c.id, cr_user=request.user.id).count()==0:
            coming_crs.append(c.id)
        else:
            coming_crs.append(False)
    ongoing_left = []
    coming_left = []
    now = datetime.datetime.now()
    for c in coming_contests:
        time = minutes_between(now, c.contest_start_time)
        coming_left.append(time)
    for c in ongoing_contest:
        time = minutes_between(now, c.contest_end_time)
        ongoing_left.append(time)
    return render(request, 'codeforce/current_contest.html',
        {
            'the_user': request.user.username,
            'coming_contests': coming_contests,
            'ongoing_contest': ongoing_contest,
            'ongoing_left': ongoing_left,
            'coming_left': coming_left,
            'coming_crs': coming_crs,
            'og_crs':og_crs
        })



@login_required(login_url = "codeforce:index")
def contest_result(request, cid):
    crs = ContestResults.objects.filter(cr_contest=cid).order_by('-cr_points')
    return render(request, 'codeforce/contest_rating.html',
        {
            'the_user': request.user.username,
            'crs': crs,
        })

@login_required(login_url = "codeforce:index")
def gotoproblem(request):
    problem = Problem.objects.filter(id = request.POST['pid'])[0]
    print problem.problem_title
    return render(request, 'codeforce/problem.html', 
        {
            'the_user':request.user.username,
            'problem':problem
        })

@login_required(login_url = "codeforce:index")
def submit(request, ocid):
    oc = OngoingContest.objects.filter(id=ocid)[0]
    now = timezone.now()
    if oc.oc_is_simulation or now > oc.oc_end_time:
        return render(request, 'codeforce/submit_result.html',
            {
                'the_user': request.user.username,
                'is_submit_successful': False
            })
    cr = ContestResults.objects.filter(cr_contest=oc.oc_contest.id, cr_user=oc.oc_user.id)
    user = CFUsers.objects.filter(id=request.user.id)[0]
    is_submited = False
    if cr.count()==0:
        cr = ContestResults(
            cr_contest = oc.oc_contest,
            cr_user = oc.oc_user,
            cr_points = oc.oc_points
            )
        cr.save()
    else:
        cr = cr[0]
    total = oc.oc_contest.contest_participant_num
    rank = ContestResults.objects.filter(cr_points__gt = oc.oc_points).count()
    rank += 1
    if not cr.cr_is_submited:
        cr.cr_is_submited = True
        cr.cr_points = oc.oc_points
        cr.save()
        user.user_points = user.user_points + total - rank + cr.cr_points
        user.save()
    return render(request, 'codeforce/submit_result.html',
        {
            'the_user': request.user.username,
            'is_submit_successful': True,
            'ongoing_contest': oc,
            'total': total,
            'rating': rank,
        })

@login_required(login_url = "codeforce:index")
def profile(request, uid=None):
    if uid==None:
        uid = request.user.id
    cfu = CFUsers.objects.filter(id=uid)[0]
    crs = ContestResults.objects.filter(cr_user=uid).order_by('id')
    contests = []
    standings = []
    for cr in crs:
        contests.append(cr.cr_contest)
        stand = ContestResults.objects.filter(cr_contest=cr.id, cr_points__gt=cr.cr_points).count()
        stand += 1
        standings.append(stand)
    return render(request, 'codeforce/profile.html',
        {
            'the_user': request.user,
            'cfu': cfu,
            'crs': crs,
            'contests': contests,
            'standings': standings
        })

@login_required(login_url = "codeforce:index")
def profile_edit(request):
    cfu = CFUsers.objects.filter(id=request.user.id)[0]
    return render(request, 'codeforce/profile_change.html',
        {
            'the_user': request.user,
            'cfu': cfu,
        })

@login_required(login_url = "codeforce:index")
def profile_change(request, uid):
    if len(request.POST) == 0:
        return render(request, 'codeforce/profile_change.html', {'the_user': request.user.username, 'reg_fail': False})

    email = request.POST['email']
    gender = request.POST['gender']
    loc = request.POST['location']
    try:
        user = CFUsers.objects.filter(id=uid)[0]
        user.user_email=email
        user.user_gender=gender
        user.user_location=loc
        user.save()
    except:
        e = sys.exc_info()[0]
        print e
        return render(request, 'codeforce/profile_change.html',
        {
            'the_user': request.user,
            'cfu': user,
            'is_chg_suc': False,
        })


    return render(request, 'codeforce/profile_change.html',
        {
            'the_user': request.user,
            'is_chg_suc': True,
        })



@login_required(login_url = "codeforce:index")
def search(request):
    result = None
    search_option = request.POST['search_option']
    if search_option == 'user':
        result = CFUsers.objects.filter(user_name__contains=request.POST['search_text'])
    else:
        result = Problem.objects.filter(problem_title__contains=request.POST['search_text'])
    return render(request, 'codeforce/search_result.html',
    {
        'the_user': request.user,
        'result': result,
        'type': search_option
    })












from django.shortcuts import render
from .models import Skill, Module, Job, Recommendation, AdminRequest, Message, Chat
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def test(request):
    return render(request, 'qcareers/test.html')

def home(request):
    return render(request, 'qcareers/home.html')

def searchJob(request):
    return render(request, 'qcareers/jobsearch.html', {'title':'Search Job'})

def recommendJob(request):
    context = {
        'allModules' : Module.objects.all(),
        'allSkills' : Skill.objects.all()
    }
    return render(request, 'qcareers/jobrecommendation.html', context)



def recommendedJob(request):
    print("in recommendedJob function")
    module1FromPost = request.POST['module-select1'] # getting the module that the user chose in POST REQ format
    grade1 = int(request.POST['grade1']) # getting grade for module 1

    module2FromPost = request.POST['module-select2']
    grade2 = int(request.POST['grade2']) # getting grade for module 2

    module3FromPost = request.POST['module-select3']
    grade3 = int(request.POST['grade3']) # getting grade for module 3

    print("grades: ")
    print(grade1)
    print(grade2)
    print(grade3)

    allModules = Module.objects.all() # acquring and storing all 'Modules' in dB in a list
    allJobs = Job.objects.all() # acquring and storing all 'Jobs' in dB in a list

    chosenModule1 = ""
    for mod in allModules:
        if mod.module_slug == module1FromPost:
            chosenModule1 = mod.module_name # getting the chosen module name in the correct format

    chosenModule2 = ""
    for mod in allModules:
        if mod.module_slug == module2FromPost:
            chosenModule2 = mod.module_name

    chosenModule3 = ""
    for mod in allModules:
        if mod.module_slug == module3FromPost:
            chosenModule3 = mod.module_name

    skills1FromPostList = request.POST.getlist('skills-select1') # list of skills user chose for module1
    skills2FromPostList = request.POST.getlist('skills-select2') # list of skills user chose for module2
    skills3FromPostList = request.POST.getlist('skills-select3') # list of skills user chose for module3


    #finalListOfSkills = []

    # these lists will contain graded/scored sets of skills, based on module grades
    listOf5s = [] # for grades 86+
    listOf4s = [] # for grades 70 - 85
    listOf3s = [] # for grades 60 - 69
    listOf2s = [] # for grades 50 - 59
    listOf1s = [] # for grades 40 - 49
    listOf0s = [] # for grades < 40

    # print("reached creation of the 5 lists")

    if grade1 >= 86:
        listOf5s.append(skills1FromPostList)
    elif grade1 >= 70:
        listOf4s.append(skills1FromPostList)
    elif grade1 >= 60:
        listOf3s.append(skills1FromPostList)
    elif grade1 >= 50:
        listOf2s.append(skills1FromPostList)
    elif grade1 >= 40:
        listOf1s.append(skills1FromPostList)
    else:
        listOf0s.append(skills1FromPostList)



    if grade2 >= 86:
        listOf5s.append(skills2FromPostList)
    elif grade2 >= 70:
        listOf4s.append(skills2FromPostList)
    elif grade2 >= 60:
        listOf3s.append(skills2FromPostList)
    elif grade2 >= 50:
        listOf2s.append(skills2FromPostList)
    elif grade2 >= 40:
        listOf1s.append(skills2FromPostList)
    else:
        listOf0s.append(skills2FromPostList)



    if grade3 >= 86:
        listOf5s.append(skills3FromPostList)
    elif grade3 >= 70:
        listOf4s.append(skills3FromPostList)
    elif grade3 >= 60:
        listOf3s.append(skills3FromPostList)
    elif grade3 >= 50:
        listOf2s.append(skills3FromPostList)
    elif grade3 >= 40:
        listOf1s.append(skills3FromPostList)
    else:
        listOf0s.append(skills3FromPostList)

    recommendedJobsList = [] #final list
    listOfAllJobs = []
    for job in allJobs:
        listOfAllJobs.append(job)




    if len(listOf5s) > 0:
        print(" ")
        print(" in listOf5s now")

        listOfMatchesWithJobs = []
        listOfMatchesButJobNames = []

        listWithSkills = [] # getting a list with the required skills, but in the required format
        for listOfSkills in listOf5s:
            for skillName in listOfSkills:
                listWithSkills.append(skillName)
        print("list of teh skills are: ")
        print (listWithSkills)

        for jobb in listOfAllJobs:
            print("current job is: " + jobb.job_role)
            count = 0
            for sk in jobb.skills.all():
                print("sk.skill_name: " + sk.skill_name + " is in listWithSkills ?")
                if sk.skill_name in listWithSkills:
                    count = count + 1
                    print(" yes, so we incremented count")
                    print("count is now: ")
                    print(count)
                else:
                    print(" no, its not in it supposedely")

            if count > 0:
                print(" count > 0: ")
                print(count)
                print(" appending count to listOfMAtchesWithJobs")
                print(" listOfMatchesWithJobs before appending: ")
                print(listOfMatchesWithJobs)
                listOfMatchesWithJobs.append(count)
                print(" listOfMatchesWithJobs after appending: ")
                print(listOfMatchesWithJobs)
                print(" appending jobb.job_role - " + jobb.job_role + " - to listOfMatchesButJobNames " )
                print("listOfMatchesButJobNames before appending:" )
                print(listOfMatchesButJobNames)
                listOfMatchesButJobNames.append(jobb.job_role)
                print("listOfMatchesButJobNames after appending:" )
                print(listOfMatchesButJobNames)


        for matches in listOfMatchesWithJobs:
            print(" in loop  ' for matches in listOfMatchesWithJobs '  ")
            print(" listOfMatchesWithJobs: ")
            print( listOfMatchesWithJobs)
            print(" max(  listOfMatchesWithJobs ) : ")
            print( max(  listOfMatchesWithJobs ) )
            print(" listOfMatchesWithJobs.index( max(  listOfMatchesWithJobs )  ")
            print(     listOfMatchesWithJobs.index(  max(listOfMatchesWithJobs) )   )
            indexOfMax = listOfMatchesWithJobs.index( max(  listOfMatchesWithJobs )  )
            if listOfMatchesButJobNames[indexOfMax] not in recommendedJobsList:
                print(listOfMatchesButJobNames[indexOfMax] + " not in recommendedJobsList. So adding it now...")
                recommendedJobsList.append(  listOfMatchesButJobNames[indexOfMax]  )
            else:
                print(listOfMatchesButJobNames[indexOfMax] + " should be in the final list, so not adding it ...")
            listOfMatchesWithJobs.pop(  indexOfMax    )
            listOfMatchesButJobNames.pop(  indexOfMax  )

        print("list of recommended jobs from listOf5s: ")
        print(recommendedJobsList)


    if len(listOf4s) > 0:
        print(" ")
        print(" in listOf4s now")
        listOfMatchesWithJobs = []
        listOfMatchesButJobNames = []

        listWithSkills = [] # getting a list with the required skills, but in the required format
        for listOfSkills in listOf4s:
            for skillName in listOfSkills:
                listWithSkills.append(skillName)

        for jobb in listOfAllJobs:
            count = 0
            for sk in jobb.skills.all():
                if sk.skill_name in listWithSkills:
                    count = count + 1

            if count > 0:
                listOfMatchesWithJobs.append(count)
                listOfMatchesButJobNames.append(jobb.job_role)

        for matches in listOfMatchesWithJobs:
            indexOfMax = listOfMatchesWithJobs.index( max(  listOfMatchesWithJobs )  )
            if listOfMatchesButJobNames[indexOfMax] not in recommendedJobsList:
                print(listOfMatchesButJobNames[indexOfMax] + " not in recommendedJobsList. So adding it now...")
                recommendedJobsList.append(  listOfMatchesButJobNames[indexOfMax]  )
            else:
                print(listOfMatchesButJobNames[indexOfMax] + " should be in the final list, so not adding it ...")
            listOfMatchesWithJobs.pop(  indexOfMax    )
            listOfMatchesButJobNames.pop(  indexOfMax  )

        print("list of recommended jobs from listOf4s: ")
        print(recommendedJobsList)


    if len(listOf3s) > 0:
        print(" ")
        print(" ")
        print(" in listOf3s now")

        listOfMatchesWithJobs = []
        listOfMatchesButJobNames = []

        listWithSkills = [] # getting a list with the required skills, but in the required format
        for listOfSkills in listOf3s:
            for skillName in listOfSkills:
                listWithSkills.append(skillName)
        print("list of the skills are: ")
        print (listWithSkills)

        for jobb in listOfAllJobs:
            print("current job is: " + jobb.job_role)
            count = 0
            for sk in jobb.skills.all():
                print("sk.skill_name: " + sk.skill_name + " is in listWithSkills ?")
                if sk.skill_name in listWithSkills:
                    count = count + 1
                    print(" yes, so we incremented count")
                    print("count is now: ")
                    print(count)
                else:
                    print(" no, its not in it supposedely")

            if count > 0:
                print(" count > 0: ")
                print(count)
                print(" appending count to listOfMAtchesWithJobs")
                print(" listOfMatchesWithJobs before appending: ")
                print(listOfMatchesWithJobs)
                listOfMatchesWithJobs.append(count)
                print(" listOfMatchesWithJobs after appending: ")
                print(listOfMatchesWithJobs)
                print(" appending jobb.job_role - " + jobb.job_role + " - to listOfMatchesButJobNames " )
                print("listOfMatchesButJobNames before appending:" )
                print(listOfMatchesButJobNames)
                listOfMatchesButJobNames.append(jobb.job_role)
                print("listOfMatchesButJobNames after appending:" )
                print(listOfMatchesButJobNames)


        for matches in listOfMatchesWithJobs:
            print(" in loop  ' for matches in listOfMatchesWithJobs '  ")
            print(" listOfMatchesWithJobs: ")
            print( listOfMatchesWithJobs)
            print(" max(  listOfMatchesWithJobs ) : ")
            print( max(  listOfMatchesWithJobs ) )
            print(" listOfMatchesWithJobs.index( max(  listOfMatchesWithJobs )  ")
            print(     listOfMatchesWithJobs.index(  max(listOfMatchesWithJobs) )   )
            indexOfMax = listOfMatchesWithJobs.index( max(  listOfMatchesWithJobs )  )
            if listOfMatchesButJobNames[indexOfMax] not in recommendedJobsList:
                print(listOfMatchesButJobNames[indexOfMax] + " not in recommendedJobsList. So adding it now...")
                recommendedJobsList.append(  listOfMatchesButJobNames[indexOfMax]  )
            else:
                print(listOfMatchesButJobNames[indexOfMax] + " should be in the final list, so not adding it ...")
            listOfMatchesWithJobs.pop(  indexOfMax    )
            listOfMatchesButJobNames.pop(  indexOfMax  )

        print("list of recommended jobs from listOf3s: ")
        print(recommendedJobsList)

    if len(listOf2s) > 0:
        print(" ")
        print(" in listOf2s now")

        listOfMatchesWithJobs = []
        listOfMatchesButJobNames = []

        listWithSkills = [] # getting a list with the required skills, but in the required format
        for listOfSkills in listOf2s:
            for skillName in listOfSkills:
                listWithSkills.append(skillName)
        print("list of teh skills are: ")
        print (listWithSkills)

        for jobb in listOfAllJobs:
            print("current job is: " + jobb.job_role)
            count = 0
            for sk in jobb.skills.all():
                print("sk.skill_name: " + sk.skill_name + " is in listWithSkills ?")
                if sk.skill_name in listWithSkills:
                    count = count + 1
                    print(" yes, so we incremented count")
                    print("count is now: ")
                    print(count)
                else:
                    print(" no, its not in it supposedely")

            if count > 0:
                print(" count > 0: ")
                print(count)
                print(" appending count to listOfMAtchesWithJobs")
                print(" listOfMatchesWithJobs before appending: ")
                print(listOfMatchesWithJobs)
                listOfMatchesWithJobs.append(count)
                print(" listOfMatchesWithJobs after appending: ")
                print(listOfMatchesWithJobs)
                print(" appending jobb.job_role - " + jobb.job_role + " - to listOfMatchesButJobNames " )
                print("listOfMatchesButJobNames before appending:" )
                print(listOfMatchesButJobNames)
                listOfMatchesButJobNames.append(jobb.job_role)
                print("listOfMatchesButJobNames after appending:" )
                print(listOfMatchesButJobNames)


        for matches in listOfMatchesWithJobs:
            print(" in loop  ' for matches in listOfMatchesWithJobs '  ")
            print(" listOfMatchesWithJobs: ")
            print( listOfMatchesWithJobs)
            print(" max(  listOfMatchesWithJobs ) : ")
            print( max(  listOfMatchesWithJobs ) )
            print(" listOfMatchesWithJobs.index( max(  listOfMatchesWithJobs )  ")
            print(     listOfMatchesWithJobs.index(  max(listOfMatchesWithJobs) )   )
            indexOfMax = listOfMatchesWithJobs.index( max(  listOfMatchesWithJobs )  )
            if listOfMatchesButJobNames[indexOfMax] not in recommendedJobsList:
                print(listOfMatchesButJobNames[indexOfMax] + " not in recommendedJobsList. So adding it now...")
                recommendedJobsList.append(  listOfMatchesButJobNames[indexOfMax]  )
            else:
                print(listOfMatchesButJobNames[indexOfMax] + " should be in the final list, so not adding it ...")
            listOfMatchesWithJobs.pop(  indexOfMax    )
            listOfMatchesButJobNames.pop(  indexOfMax  )

        print("list of recommended jobs from listOf2s: ")
        print(recommendedJobsList)


    if len( recommendedJobsList ) > 2:

        r1 = recommendedJobsList[0]
        r2 = recommendedJobsList[1]
        r3 = recommendedJobsList[2]
        userRecommendationObj = Recommendation.objects.create(
            user = request.user,
            recOne = r1,
            recTwo = r2,
            recThree = r3,
            #dateAndTimeOfRec =
        )
        userRecommendationObj.save()

    elif len( recommendedJobsList ) == 0:
        recommendedJobsList.append("Unable to find suitable job role from supplied grades and chosen skills")
        recommendedJobsList.append("Unable to find suitable job role from supplied grades and chosen skills")
        recommendedJobsList.append("Unable to find suitable job role from supplied grades and chosen skills")

    elif len( recommendedJobsList ) == 1:
        recommendedJobsList.append("Unable to find suitable job role from supplied grades and chosen skills")
        recommendedJobsList.append("Unable to find suitable job role from supplied grades and chosen skills")

    elif len( recommendedJobsList ) == 2:
        recommendedJobsList.append("Unable to find suitable job role from supplied grades and chosen skills")



    context= {
        'recommendedJobsList':recommendedJobsList
    }
    return render(request, 'qcareers/recommendedjob.html', context)


    return render(request, 'qcareers/recommendedjob.html')




def recommendedJobOld(request):
    module1FromPost = request.POST['module-select1'] # getting the module that the user chose in POST REQ format
    module2FromPost = request.POST['module-select2']
    module3FromPost = request.POST['module-select3']
    allModules = Module.objects.all() # acquring and storing all 'Modules' in dB in a list
    allJobs = Job.objects.all() # acquring and storing all 'Jobs' in dB in a list

    chosenModule1 = ""
    for mod in allModules:
        if mod.module_slug == module1FromPost:
            chosenModule1 = mod.module_name # getting the chosen module name in the correct format

    chosenModule2 = ""
    for mod in allModules:
        if mod.module_slug == module2FromPost:
            chosenModule2 = mod.module_name

    chosenModule3 = ""
    for mod in allModules:
        if mod.module_slug == module3FromPost:
            chosenModule3 = mod.module_name

    skills1FromPostList = request.POST.getlist('skills-select1') # list of skills user chose
    skills2FromPostList = request.POST.getlist('skills-select2')
    skills3FromPostList = request.POST.getlist('skills-select3')


    finalListOfSkills = []

    for skill in skills1FromPostList:
        if skill not in finalListOfSkills:
            finalListOfSkills.append(skill)

    for skill in skills2FromPostList:
        if skill not in finalListOfSkills:
            finalListOfSkills.append(skill)

    for skill in skills3FromPostList:
        if skill not in finalListOfSkills:
            finalListOfSkills.append(skill)


    listOfAllJobs = []
    for job in allJobs:
        listOfAllJobs.append(job)

    listOfMatchesWithJobs = []

    recommendedJobsList = []

    for jobb in listOfAllJobs:
        count = 0
        for sk in jobb.skills.all():
            if sk.skill_name in finalListOfSkills:
                count = count + 1

        listOfMatchesWithJobs.append(count)

    for matches in listOfMatchesWithJobs:

        indexOfMax = listOfMatchesWithJobs.index(max(listOfMatchesWithJobs))

        recommendedJobsList.append(listOfAllJobs[indexOfMax])


        listOfMatchesWithJobs.pop(  indexOfMax    )


        listOfAllJobs.pop(indexOfMax)

    r1 = recommendedJobsList[0].job_role
    r2 = recommendedJobsList[1].job_role
    r3 = recommendedJobsList[2].job_role
    userRecommendationObj = Recommendation.objects.create(
        user = request.user,
        recOne = r1,
        recTwo = r2,
        recThree = r3,
        #dateAndTimeOfRec =
    )

    userRecommendationObj.save()

    context= {
        'recommendedJobsList':recommendedJobsList
    }
    return render(request, 'qcareers/recommendedjob.html', context)





#def getSkillsForModule(request):
#    moduleReqObj = request.GET['chosenModule']
#    module = Module.objects.all(module_name=moduleReqObj)
#    data = []
#
#    for skill in module.skills:
#        data.append(skill)
#
#    serialisedData = serializers.serialize("json", data, indent = 2, use_natural_foreign_keys=True, use_natural_primary_keys=True)
#    return JsonResponse(serialisedData, safe=False)


def manageSkills(request):
    allSkills = Skill.objects.all()
    if request.method == 'POST' and 'addSkillButton' in request.POST:
        skillText = request.POST['skillName']
        skillObject = Skill(skill_name=skillText, skill_slug=skillText.replace(" ",""))

        skillIsPresent = False
        for skill in allSkills:
            if skill.skill_name == skillObject.skill_name:
                skillIsPresent = True

        if skillIsPresent == False:
            skillObject.save()
            allSkills = Skill.objects.all()
            context = {
                'outcome' : 'Successfully added new skill ' + skillText + '!',
                'state' : 'success-add',
                'skills' : allSkills
            }
            return render(request, 'qcareers/manageskills.html', context)

        context = {
            'outcome' : 'Unsuccessful! Skill ' + skillText + ' already exists.',
            'state': 'fail-add',
            'skills' : allSkills
        }
        return render(request, 'qcareers/manageskills.html', context)

    elif request.method == 'POST' and 'deleteSkillButton' in request.POST:
        chosenSkill = ""
        skillFromPost = request.POST['skillsSelect']
        for skill in allSkills:
            if skill.skill_slug == skillFromPost:
                chosenSkill = skill.skill_name # getting the chosen module name in the correct format

        skillToDelete = Skill.objects.get(skill_name=chosenSkill)
        skillToDelete.delete()
        allSkills = Skill.objects.all()
        context = {
            'outcomeFail' : 'Successfully deleted skill ' + chosenSkill + '!',
            'state': 'success-delete',
            'skills' : allSkills
        }
        return render(request, 'qcareers/manageskills.html', context)

    elif request.method == 'GET':
        context = {
            'skills' : allSkills
        }
        return render(request, 'qcareers/manageskills.html', context)
    #return render(request, 'qcareers/addnewskill.html')


def manageModules(request):
    allSkills = Skill.objects.all()
    allModules = Module.objects.all()
    context = {
        'skills' : allSkills,
        'modules' : allModules
    }

    if request.method == 'POST' and 'addModuleButton' in request.POST:
        module = request.POST['moduleName'] #string form
        moduleInStringFormat = "" + module
        skillsFromPostList = request.POST.getlist('skillsSelect')

        moduleIsPresent = False
        for modulee in allModules:
            if modulee.module_name == moduleInStringFormat:
                moduleIsPresent = True

        if moduleIsPresent == False:
            slug = moduleInStringFormat.replace(" ", "")

            moduleObject = Module.objects.create(
                module_name=module,
                module_slug=slug,
            )

            moduleObject.save()
            print ("Obj suposedely saved first time")

            print("skillsFromPostList: ")
            print (skillsFromPostList)
            print("")

            for skill in allSkills:
                print("Skill: ")
                print (skill)
                if skill.skill_slug in skillsFromPostList:
                    print ("Skill is matched")
                    moduleObject.skills.add(skill)

            print ("Skills added supposedely")
            print(moduleObject.skills)

            moduleObject.save()
            allModules = Module.objects.all()
            allSkills = Skill.objects.all()
            print("obj supposedely saved again to dB")

            context = {
                'outcome' : 'Successfully added new module ' + module + '!',
                'state' : 'success-add',
                'skills' : allSkills,
                'modules' : allModules
            }
            return render(request, 'qcareers/managemodules.html', context)

        context = {
            'outcome' : 'Unsuccessful! Module ' + module + ' already exists.',
            'state' : 'fail-add',
            'skills' : allSkills,
            'modules' : allModules
        }
        return render(request, 'qcareers/managemodules.html', context)


    elif request.method == 'POST' and 'deleteModuleButton' in request.POST:
        chosenModule = ""
        moduleFromPost = request.POST['modulesSelect']
        for module in allModules:
            if module.module_slug == moduleFromPost:
                chosenModule = module.module_name # getting the chosen module name in the correct format

        moduleToDelete = Module.objects.get(module_name=chosenModule)
        moduleToDelete.delete()
        allModules = Module.objects.all()
        allSkills = Skill.objects.all()
        context = {
            'outcomeDeleted' : 'Successfully deleted module ' + chosenModule + '!',
            'state' : 'success-delete',
            'skills' : allSkills,
            'modules' : allModules
        }
        return render(request, 'qcareers/managemodules.html', context)

    elif request.method == 'GET':
        return render(request, 'qcareers/managemodules.html', context)

    return render(request, 'qcareers/managemodules.html', context)




def manageJobs(request):
    allSkills = Skill.objects.all()
    allJobs = Job.objects.all()
    context = {
        'skills' : allSkills,
        'jobs' : allJobs
    }

    if request.method == 'POST' and 'addJobButton' in request.POST:
        job = request.POST['jobName'] #string form
        #moduleInStringFormat = "" + module
        skillsFromPostList = request.POST.getlist('skillsSelect')

        jobIsPresent = False
        for jobb in allJobs:
            if jobb.job_role == job:
                jobIsPresent = True

        if jobIsPresent == False:
            slug = job.replace(" ", "")

            jobObject = Job.objects.create(
                job_role=job,
                job_slug=slug,
            )

            jobObject.save()
            print ("Obj suposedely saved first time")

            print("skillsFromPostList: ")
            print (skillsFromPostList)
            print("")

            for skill in allSkills:
                print("Skill: ")
                print (skill)
                if skill.skill_slug in skillsFromPostList:
                    print ("Skill is matched")
                    jobObject.skills.add(skill)

            print ("Skills added supposedely")
            #print(moduleObject.skills)

            jobObject.save()
            allSkills = Skill.objects.all()
            allJobs = Job.objects.all()
            print("obj supposedely saved again to dB")

            context = {
                'outcome' : 'Successfully added new job role ' + job + '!',
                'state' : 'success-add',
                'skills' : allSkills,
                'jobs' : allJobs
            }
            return render(request, 'qcareers/managejobs.html', context)

        context = {
            'outcome' : 'Unsuccessful! ' + job + ' job role already exists.',
            'state' : 'fail-add',
            'skills' : allSkills,
            'jobs' : allJobs
        }
        return render(request, 'qcareers/managejobs.html', context)


    elif request.method == 'POST' and 'deleteJobButton' in request.POST:
        chosenJob = ""
        jobFromPost = request.POST['jobsSelect']

        for jobb in allJobs:
            if jobb.job_slug == jobFromPost:
                chosenJob = jobb.job_role # getting the chosen job name in the correct format

        jobToDelete = Job.objects.get(job_role=chosenJob)
        jobToDelete.delete()
        allSkills = Skill.objects.all()
        allJobs = Job.objects.all()
        context = {
            'outcomeDeleted' : 'Successfully deleted job role ' + chosenJob + '!',
            'state' : 'success-delete',
            'skills' : allSkills,
            'jobs' : allJobs
        }
        return render(request, 'qcareers/managejobs.html', context)

    elif request.method == 'GET':
        return render(request, 'qcareers/managejobs.html', context)

    return render(request, 'qcareers/managejobs.html', context)


def myRecommendations(request):
    outcome = ""
    state=""
    if request.method == 'POST':
        idOfRecToDel = request.POST['recIdToDelText']

        if Recommendation.objects.filter(id=idOfRecToDel).exists():
            recommendationToDel = Recommendation.objects.get(id=idOfRecToDel)

            if recommendationToDel.user == request.user:
                recommendationToDel.delete()
                outcome = "Successfully deleted recommendation with ID " + idOfRecToDel + "!"
                state="success"

            else:
                outcome = "Unsuccessful! Recommendation with ID " + idOfRecToDel + " does not exist"
                state = "fail"

        else:
            outcome = "Unsuccessful! Recommendation with ID " + idOfRecToDel + " does not exist"
            state = "fail"

    allUserRecommendationsObjectsList = Recommendation.objects.all()

    usersRecommendationsObjectsList = []

    for recommendationObj in allUserRecommendationsObjectsList:
        if recommendationObj.user == request.user:
            usersRecommendationsObjectsList.append(recommendationObj)

    context = {
        'recommendationsObjList' : usersRecommendationsObjectsList,
        'outcome' : outcome,
        'state' : state
    }
    return render(request, 'qcareers/usersrecommendations.html', context)



def requestAdmin(request):
    state = ""

    if request.method == 'POST':
        firstNamePost = request.POST['firstNameText'] #string form
        lastNamePost = request.POST['lastNameText']
        messageTextPost = request.POST['messageText']

        adminRequestObject = AdminRequest.objects.create(
            user = request.user,
            firstName = firstNamePost,
            lastName = lastNamePost,
            message = messageTextPost,
            # dateAdminRequested done automatically
        )

        adminRequestObject.save()
        state = "one request pending"
        context = {
            'outcome' : 'Successfully sent request!',
            'state' : state
        }
        return render(request, 'qcareers/requestadmin.html', context)

    allAdminRequests = AdminRequest.objects.all()
    userHasPengingRequest = False

    for adminRequest in allAdminRequests:
        if adminRequest.user == request.user:
            userHasPengingRequest = True

    if userHasPengingRequest == True:
        state = "one request pending"
    else:
        state = "no requests pending"

    context2 = {
        'state' : state
    }

    return render(request, 'qcareers/requestadmin.html', context2)

def manageRequestsGet(request):
    allAdminRequestsObjectsList = AdminRequest.objects.all()
    adminRequestsList = []

    if request.method == 'GET':
        for adminRequestsObject in allAdminRequestsObjectsList:
            adminRequestsList.append(adminRequestsObject)

        context={
            'adminRequestsList' : adminRequestsList
        }
        return render(request, 'qcareers/managerequests.html', context)

    return render(request, 'qcareers/managerequests.html')

def manageRequestsPost(request, admReqId):
    if request.method == 'POST':
        outcome= ""
        state=""
        admReqObjToManage = AdminRequest.objects.get(id=admReqId)

        if 'reject' in request.POST:
            admReqObjToManage.delete()
            outcome = "Successfully rejected request!"
            state="rejected"

        else:
            userToAdmit = User.objects.get(id = admReqObjToManage.user.id)
            print("user to admit : ")
            print(userToAdmit)
            userToAdmit.is_superuser = True
            userToAdmit.save()
            admReqObjToManage.delete()
            outcome = "Successfully approved user as admin"
            state = "approved"

        allAdminRequestsObjectsList = AdminRequest.objects.all()
        adminRequestsList = []

        for adminRequestsObject in allAdminRequestsObjectsList:
            adminRequestsList.append(adminRequestsObject)

        context={
            'adminRequestsList' : adminRequestsList,
            'outcome' : outcome,
            'state' : state
        }
        return render(request, 'qcareers/managerequests.html', context)

    return render(request, 'qcareers/managerequests.html')


def ajax(request):
    print("this def is called")
    return render(request, 'qcareers/ajax.html')

def ajaxData(request):
    print("ajax def is called")
    if request.method == 'GET':
        return JsonResponse({
            'id' : 'ghana'
        })




def supportPage(request):
    if request.method == 'POST':

        allChatObjects = Chat.objects.all()
        usersChatExists = False
        for chat in allChatObjects:
            if chat.user == request.user:
                usersChatExists = True

        if usersChatExists == False:
            allUsers = User.objects.all()
            adminUser = None
            for usr in allUsers:
                if usr.get_username()=="admin":
                    adminUser = usr


            adminDefaultMessage = Message.objects.create(
                sender = adminUser,
                receiver = request.user,
                message = "Hi, this is the start of our chat. How can i help?"
            )
            adminDefaultMessage.save()


            newChat = Chat()
            newChat.user = request.user
            newChat.save()
            newChat.messages.add(adminDefaultMessage)
            newChat.save()

            #newChat = Chat.objects.create(
            #    user = request.user,
            #    messages = []
            #)

        context = {
            'username' : request.user.get_username()
        }
        return render(request, 'qcareers/supportchat.html', context)

    return render(request, 'qcareers/supportpage.html')

def supportChat(request):
#    if request.method == 'GET':
#        context = {
#            'user' : request.user.get_username()
#        }
    return render(request, 'qcareers/supportchat.html')


def getMessages(request):
    userInvolved = request.GET['userInv']
    print("userInvolved : " + userInvolved)
    allChats = Chat.objects.all()
    correctChat = None

    for chat in allChats:
        if chat.user.get_username() == userInvolved:
            #print("chat.user.get_username() :" )
            #print (chat.user.get_username())
            #print ("and")
            #print("userInvolved :")
            #print (userInvolved)
            correctChat = chat

    #print (correctChat.messages.all())

    listOfMessagesObjects = correctChat.messages.all()

    listOfMessages = []
    listOfUserOrder = []
    listOfMessagesTimes = []

    for messageObject in listOfMessagesObjects:
        listOfMessages.append(messageObject.message)
        if messageObject.sender.get_username() == userInvolved:
            listOfUserOrder.append("user")
        else:
            listOfUserOrder.append("admin")

        listOfMessagesTimes.append(messageObject.dateAndTimeSent.strftime("%H:%M:%S"))

    #print("listOfMessages: ")
    #print(listOfMessages)

    #print ("reached here ")
    messages = {
        'messages' : listOfMessages,
        'order' : listOfUserOrder,
        'user' : correctChat.user.get_username(),
        'times' : listOfMessagesTimes
    }
    return JsonResponse(messages)


def checkForNotifs(request):
    #print("request been made. In def")
    if request.user.is_authenticated == False:
        b = {
            'c' : 'c'
        }
        return JsonResponse(b)

    #print("surpassed authenticity. So user is deffo logged in")

    userFromPost = request.GET['user']

    loggedInUser = User.objects.get(username=userFromPost)
    userIsAdmin = ""
    if loggedInUser.is_superuser:
        userIsAdmin = "true"
    else:
        userIsAdmin = "false"

    #print("userIsAdmin: " + userIsAdmin)

    #now need to check if they are admin and they have any requests pending
    if userIsAdmin == "true":

        #print("in if st for usr is adm")

        allAdminReqs = AdminRequest.objects.all()
        hasReqs = "false"
        if len(allAdminReqs) > 0 :
            hasReqs = "true"

        #print("hasReqs: " + hasReqs)

        #now need to check if admins have any active chats
        allChats = Chat.objects.all()
        hasChats = "false"
        if len(allChats) > 0:
            hasChats = "true"

        #print("hasChats: " + hasChats)


        context = {
            'userIsAdmin' : userIsAdmin,
            'hasReqs' : hasReqs,
            'hasChats' : hasChats
        }
        #print(context)
        return JsonResponse(context)

    if userIsAdmin == "false":
        #userChat = Chat.objects.get(user=request.user)
        allChatss = Chat.objects.all()
        hasChatss = "false"
        for chat in allChatss:
            if chat.user == request.user:
                hasChatss = "true"

        cont = {
            'hasChatss' : hasChatss
        }
        return JsonResponse(cont)

    con = {
        'c' : 'c'
    }
    return JsonResponse(con)







@csrf_exempt
def postMessage(request):
    messageFromPost = request.POST['msg']
    #userFromPost = request.POST['user']     #not even using this lol

    allUsers = User.objects.all()
    adminUser = None
    for usr in allUsers:
        if usr.get_username()=="admin":
            adminUser = usr

    messageObject = Message.objects.create(
        sender=request.user,
        receiver = adminUser,
        message = messageFromPost
    )
    messageObject.save()

    usersChatObject = Chat.objects.get(user=request.user)
    usersChatObject.messages.add(messageObject)
    usersChatObject.save()

    empty = {
        'empty' : ' '
    }
    return JsonResponse(empty)







def supportPageForAdmins(request):
    allChatObjects = Chat.objects.all()
    #listOfUsersWithChats = []
    listOfUsersObjectsWithChats = []

    for chat in allChatObjects:
        listOfUsersObjectsWithChats.append(chat.user)

    context = {
        'usersList' : listOfUsersObjectsWithChats
    }

    return render(request, 'qcareers/supportpageforadmins.html', context)

def supportChatForAdmins(request, userId):
    chatObject = Chat.objects.get(user=userId)
    user = User.objects.get(id=userId)
    usersUsername = user.get_username()
    print("username of the user is :: ")
    print (usersUsername)
    print("id of the user is :: ")
    print (userId)
    #print (user.pk)

    context = {
        'username' : usersUsername
    }

    return render(request, 'qcareers/supportchatforadmins.html', context)


def getMessagesForAdmins(request):
    return JsonResponse("messages")


@csrf_exempt
def postMessageForAdmins(request):
    messageFromPost = request.POST['msg']
    userFromPost = request.POST['user']  # this is basc the users username

    allUsers = User.objects.all()
    adminUser = None
    for usr in allUsers:
        if usr.get_username()=="admin":
            adminUser = usr

    usersUserObject = User.objects.get(username=userFromPost)



    messageObject = Message.objects.create(
        sender=adminUser,
        receiver = usersUserObject,
        message = messageFromPost
    )
    messageObject.save()

    usersChatObject = Chat.objects.get(user=usersUserObject)
    usersChatObject.messages.add(messageObject)
    usersChatObject.save()

    empty = {
        'empty' : ' '
    }
    return JsonResponse(empty)

def deleteChat(request, username):
    print("username of chat to delete: ")
    print (username)

    allUsers = User.objects.all()
    correctUser = None
    for usr in allUsers:
        if usr.get_username() == username:
            correctUser = usr


    chatObj = Chat.objects.get(user = correctUser)

    listOfMessageObjectsIdsToDelete = []

    for message in chatObj.messages.all():
        listOfMessageObjectsIdsToDelete.append(message.id)

    print("IDs to Delete: ")
    print(listOfMessageObjectsIdsToDelete)

    print("Chat to Delete: ")
    print(chatObj)

    chatObj.delete()

    for msgId in listOfMessageObjectsIdsToDelete:
        messageObjToDel = Message.objects.get(id=msgId)
        messageObjToDel.delete()

    if request.user.is_superuser:
        allChatObjects = Chat.objects.all()
        listOfUsersObjectsWithChats = []

        for chat in allChatObjects:
            listOfUsersObjectsWithChats.append(chat.user)

        context = {
            'state' : 'deleted',
            'outcome' : 'Successfully deleted chat!',
            'usersList' : listOfUsersObjectsWithChats
        }
        return render(request, 'qcareers/supportpageforadmins.html', context)
    else:
        return render(request, 'qcareers/supportpage.html')

from django.shortcuts import render, redirect
from app.forms import UserForm
from app.queries import find_match

# Create your views here.
def userView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():

            user_age = form.cleaned_data["age"]
            user_email = form.cleaned_data["email"]
            user_gender = form.cleaned_data["gender"]
            user_governorate = form.cleaned_data["governorate"]
            user_cs_field = form.cleaned_data["cs_field"]
            user_experience_levels = form.cleaned_data["experience_levels"]
            buddy_age = form.cleaned_data["buddy_age"]
            buddy_gender = form.cleaned_data["buddy_gender"]
            buddy_governorate = form.cleaned_data["buddy_governorate"]

            # Call the find_match function to get the data
            result = find_match(
               user_age, user_gender, user_governorate, user_cs_field, user_experience_levels, buddy_age, buddy_gender,
                buddy_governorate
            )

            if isinstance(result, tuple) and len(result) == 4:
                name, gender, twitter_link, github_link = result
                context = {
                    'form': form,
                    'name': name,
                    'gender': gender,
                    'twitter_link': twitter_link,
                    'github_link': github_link,
                }
                return render(request, 'res.html', context)
            else:
                form.save()
                return render(request, 'res.html', {'form': form})
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})
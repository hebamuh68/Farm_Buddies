from app.models import UserModel

def find_match(user_age, user_gender, user_governorate, user_cs_field, user_experience_levels, buddy_age,
               buddy_gender, buddy_governorate):
    match_criteria = {'cs_field': user_cs_field, 'experience_levels': user_experience_levels}

    if buddy_age == 'Any':
        match_criteria['buddy_age'] = 'Any'
    else:
        match_criteria['age'] = buddy_age
        match_criteria['buddy_age__in'] = ['Any', user_age]

    if buddy_gender == 'Any':
        match_criteria['buddy_gender'] = 'Any'
    else:
        match_criteria['gender'] = buddy_gender
        match_criteria['buddy_gender__in'] = ['Any', user_gender]

    if buddy_governorate == 'Any':
        match_criteria['buddy_governorate'] = 'Any'
    else:
        match_criteria['governorate'] = buddy_governorate
        match_criteria['buddy_governorate__in'] = ['Any', user_governorate]

    # Remove None values from the dictionary
    match_criteria = {key: value for key, value in match_criteria.items() if value is not None}

    # Exclude the user with the given user_id
    match = UserModel.objects.filter(**match_criteria).first()

    if match:
        name = match.name
        twitter_link = match.twitter_link
        github_link = match.github_link
        gender = match.gender

        # Delete the matched user
        match.delete()
        return name, gender, twitter_link, github_link
    else:
        return None
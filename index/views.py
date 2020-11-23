from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from django import forms
from django.views.decorators.csrf import csrf_exempt
from index.forms import SearchForm


# Create your views here.


class SearchView(ListView):
    template_name = "index/search.html"
    industryID = '0'
    keywordID = '0'
    ratingID = '0'

    def __init__(self, **kwargs):
        super(ListView, self).__init__(**kwargs)

    def setup(self, request, *args, **kwargs):
        super(ListView, self).setup(request, *args, **kwargs)
        self.industryID = request.GET.get("industryID", self.industryID)
        self.keywordID = request.GET.get("keywordID", self.keywordID)
        self.ratingID = request.GET.get("ratingID", self.ratingID)

    def get_queryset(self):
        positions = [
            {
                'id': 1,
                'position': 'Data Scientist',
                'company': 'Wayfair',
                'rating': '4.9',
                'ratingID': '5',
                'industry': '7',
                'keyword': '1'
            },
            {
                'id': 2,
                'position': 'PT Co-op',
                'company': 'PT Arlington',
                'rating': '4.7',
                'ratingID': '5',
                'industry': '8',
                'keyword': '1'
            },
            {
                'id': 3,
                'position': 'UI/UX Design Co-op',
                'company': 'NetBrain',
                'rating': '4.7',
                'ratingID': '5',
                'industry': '2',
                'keyword': '2'
            },
            {
                'id': 4,
                'position': 'Software Engineering Co-op',
                'company': 'ASICS',
                'rating': '3.9',
                'ratingID': '4',
                'industry': '7',
                'keyword': '1'
            },
        ]

        qs = []
        if self.industryID != '0':
            filtered_positions = []
            for p in positions:
                if p.get('industry') == self.industryID:
                    filtered_positions.append(p)
            qs = filtered_positions


        if self.keywordID != '0':
            filter_keywords = []
            positions_to_filter = []
            if qs == []:
                positions_to_filter = positions
            else:
                positions_to_filter = qs

            for p in positions_to_filter:
                if p.get('keyword') == self.keywordID:
                    filter_keywords.append(p)

            qs = filter_keywords

        if self.ratingID != '0':
            filter_keywords = []
            positions_to_filter = []
            if qs == []:
                positions_to_filter = positions
            else:
                positions_to_filter = qs

            for p in positions_to_filter:
                if p.get('ratingID') == self.ratingID:
                    filter_keywords.append(p)

            qs = filter_keywords

        if qs == []:
            qs = positions

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        industry_list = [
            {
                'id': '1',
                'name': 'Accounting',
                'abbrev': 'acct',
            },
            {
                'id': '2',
                'name': 'Arts & Design',
                'abbrev': 'a_and_d',
            },
            {
                'id': '3',
                'name': 'Cybersecurity',
                'abbrev': 'cyber',
            },
            {
                'id': '4',
                'name': 'Engineering',
                'abbrev': 'eng',
            },
            {
                'id': '5',
                'name': 'Finance',
                'abbrev': 'fin',
            },
            {
                'id': '6',
                'name': 'Human Resources',
                'abbrev': 'hr',
            },
            {
                'id': '7',
                'name': 'Information Technology',
                'abbrev': 'it',
            },
            {
                'id': '8',
                'name': 'Physical Therapy',
                'abbrev': 'pt',
            },
        ]

        keyword_list = [
            {
                'id': '1',
                'name': 'fun',
            },
            {
                'id': '2',
                'name': 'hardworking',
            },
            {
                'id': '3',
                'name': 'uptight',
            }
        ]

        rating_list = [
            {
                'id': '1',
                'name': '0-0.99',
            },
            {
                'id': '2',
                'name': '1.00-1.99',
            },
            {
                'id': '3',
                'name': '2.00-2.99',
            },
            {
                'id': '4',
                'name': '3.00-3.99',
            },
            {
                'id': '5',
                'name': '4.00-5.00',
            }
        ]

        context['industryID'] = self.industryID
        context['industries'] = industry_list
        context['keywordID'] = self.keywordID
        context['keywords'] = keyword_list
        context['ratingID'] = self.ratingID
        context['ratings'] = rating_list
        return context


class IndexView(TemplateView):
    template_name = "index/index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

class ManagerView(TemplateView):
    template_name = "index/manager.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

class PositionView(TemplateView):
    template_name = "index/manager_position.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

class CreateRatingForm(forms.Form):
    comments = forms.CharField(required=False)


class RatingFormView(FormView):
    form_class = CreateRatingForm
    template_name = "index/ratingform.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form_categories = [
            {
                'name': 'Responsibility',
                'description': 'Your work consisted of meaningful tasks that influenced your team and/or company.',
                'keyword': 'responsibility',
                'popover': [
                    {
                        'value': 'Strongly Disagree',
                        'description': "Your works' quality does not matter at all.",
                    },
                    {
                        'value': 'Neutral',
                        'description': "Your work is checked and approved before submitting.",
                    },
                    {
                        'value': 'Strongly Agree',
                        'description': 'Your work is carefully checked and approved before submitting.',
                    },
                ]
            },
            {
                'name': 'Supervisor',
                'description': 'Your supervisor communicated with you regularly.',
                'keyword': 'supervisor',
                'popover': [
                    {
                        'value': 'Strongly Disagree',
                        'description': 'Your supervisor never checks in with you.',
                    },
                    {
                        'value': 'Neutral',
                        'description': 'Your supervisor sometimes checks in with you.',
                    },
                    {
                        'value': 'Strongly Agree',
                        'description': 'Your supervisor frequently checks in with you.',
                    },
                ]
            },
            {
                'name': 'Teamwork',
                'description': 'Your team collaborated well.',
                'keyword': 'teamwork',
                'popover': [
                    {
                        'value': 'Strongly Disagree',
                        'description': 'You do your own work and there is no collaboration.',
                    },
                    {
                        'value': 'Neutral',
                        'description': 'There is some collaboration.',
                    },
                    {
                        'value': 'Strongly Agree',
                        'description': 'You frequently work in a team.',
                    },
                ]
            },
            {
                'name': 'Compensation',
                'description': 'Your pay was appropriate for your role and experience.',
                'keyword': 'compensation',
                'popover': [
                    {
                        'value': 'Strongly Disagree',
                        'description': 'You are not satisfied with your compensation at all.',
                    },
                    {
                        'value': 'Neutral',
                        'description': 'You are somewhat satisfied with your compensation.',
                    },
                    {
                        'value': 'Strongly Agree',
                        'description': 'You are 100% satisfied with your compensation.',
                    },
                ]
            },
            {
                'name': 'Benefits',
                'description': 'The position came with additional benefits (ex: T-Pass, healthcare benefits, lunches, etc.)',
                'keyword': 'benefits',
                'popover': [
                    {
                        'value': 'Strongly Disagree',
                        'description': 'There are no additional benefits.',
                    },
                    {
                        'value': 'Neutral',
                        'description': 'There are some additional benefits.',
                    },
                    {
                        'value': 'Strongly Agree',
                        'description': 'There are many additional benefits.',
                    },
                ]
            },
            {
                'name': 'Working Hours',
                'description': 'Your working hours were as expected.',
                'keyword': 'working_hours',
                'popover': [
                    {
                        'value': 'Strongly Disagree',
                        'description': 'Your required working hours deviated from what was initially expected.',
                    },
                    {
                        'value': 'Neutral',
                        'description': 'Your working hours slightly deviated from what was expected.',
                    },
                    {
                        'value': 'Strongly Agree',
                        'description': 'Your working hours were as expected.',
                    },
                ]
            },
            {
                'name': 'Diversity',
                'description': 'Your team/department consists of a diverse group.',
                'keyword': 'diversity',
                'popover': [
                    {
                        'value': 'Strongly Disagree',
                        'description': 'Your team consisted of little to no diversity.',
                    },
                    {
                        'value': 'Neutral',
                        'description': 'Your team had some diversity.',
                    },
                    {
                        'value': 'Strongly Agree',
                        'description': 'Your team was made up of diverse cultures and backgrounds.',
                    },
                ]
            },
            {
                'name': 'Inclusivity',
                'description': 'Your team/department fostered an inclusive working environment.',
                'keyword': 'inclusivity',
                'popover': [
                    {
                        'value': 'Strongly Disagree',
                        'description': 'The work environment was not inclusive of all people and their ideas.',
                    },
                    {
                        'value': 'Neutral',
                        'description': 'The work environment was usually inclusive.',
                    },
                    {
                        'value': 'Strongly Agree',
                        'description': 'The work environment actively included everyone.',
                    },
                ]
            },
            {
                'name': 'Growth Opportunity',
                'description': 'You left your co-op with new knowledge (ex: skills, personal values, etc.)',
                'keyword': 'growth_opportunity',
                'popover': [
                    {
                        'value': 'Strongly Disagree',
                        'description': 'You learned no new things and/or you were not given the opportunity to learn.',
                    },
                    {
                        'value': 'Neutral',
                        'description': 'You learned a few new skills or personal values that you can apply in the future.',
                    },
                    {
                        'value': 'Strongly Agree',
                        'description': 'You learned many new skills and were given many learning opportunities.',
                    },
                ]
            },
        ]

        radio_buttons = [
            {
                'keyword': 's_dis',
                'value': 'strongly_disagree',
                'name': 'Strongly Disagree'
            },
            {
                'keyword': 'dis',
                'value': 'disagree',
                'name': 'Disagree'
            },
            {
                'keyword': 'n',
                'value': 'neutral',
                'name': 'Neutral'
            },
            {
                'keyword': 'ag',
                'value': 'agree',
                'name': 'Agree'
            },
            {
                'keyword': 's_ag',
                'value': 'strongly_agree',
                'name': 'Strongly Agree'
            },
        ]

        culture = {
                'name': 'Culture',
                'description': "Please select keywords that describe your team's culture. You can select as many or as few as desired.",
                'keyword': 'culture',
        }

        checkboxes = [
            {
                'keyword': 'creative',
                'name': 'Creative',
                'value': 'creative',
            },
            {
                'keyword': 'hardworking',
                'name': 'Hardworking',
                'value': 'hardworking',
            },
            {
                'keyword': 'fun',
                'name': 'Fun',
                'value': 'fun',
            },
            {
                'keyword': 'laidback',
                'name': 'Laid-Back',
                'value': 'laidback',
            },
            {
                'keyword': 'uptight',
                'name': 'Uptight',
                'value': 'uptight',
            },
        ]

        overall_rating = {
            'name': 'Overall Rating',
            'description': "Select an overall rating for this co-op experience. 5 is the highest score; 1 is the lowest.",
            'keyword': 'overall_rating'
        }

        overall_rating_values = [
            {
                'keyword': 'one',
                'name': '1',
                'value': 'one',
            },
            {
                'keyword': 'two',
                'name': '2',
                'value': 'two',
            },
            {
                'keyword': 'three',
                'name': '3',
                'value': 'three',
            },
            {
                'keyword': 'four',
                'name': '4',
                'value': 'four',
            },
            {
                'keyword': 'five',
                'name': '5',
                'value': 'five',
            },
        ]

        contact_opt_in = {
            'name': 'Contact Opt-In',
            'description': "Are you willing to be contacted by other students via email to discuss your co-op experience? Your email address will not be made public.",
            'keyword': 'contact_opt_in',
        }

        contact_opt_in_values = [
            {
                'keyword': 'yes',
                'name': 'Yes',
                'value': 'yes',
            },
            {
                'keyword': 'no',
                'name': 'No',
                'value': 'no',
            }
        ]

        context['form_categories'] = form_categories
        context['radio_buttons'] = radio_buttons
        context['culture'] = culture
        context['checkboxes'] = checkboxes
        context['overall_rating'] = overall_rating
        context['overall_rating_values'] = overall_rating_values
        context['contact_opt_in'] = contact_opt_in
        context['contact_opt_in_values'] = contact_opt_in_values
        return context


class ConstructionView(TemplateView):
    template_name = "index/construction.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

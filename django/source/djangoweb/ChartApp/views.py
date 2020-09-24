from django.shortcuts import render

# Create your views here.



def intro(request):
    return render(request, 'chart_index.html')


def line(request):

    seoul = [7.0, 6.9, 9.5, 7.0, 6.9, 9.5, 7.0, 6.9, 9.5]
    london = [9.0, 8.9, 7.5, 6.0, 8.9, 6.5, 8.0, 9.9, 5.5]

    context = {'seoul': seoul, 'london': london}
    return render(request, 'chart_line.html', context)


def bar(request):
    africa =[107,31,635,203,2]
    america = [133,156,947,408,6]
    asia = [814,841,3714,727,31]
    europe = [1216,1001,4436,738,40]
    context={'Africa' : africa,
             'America' : america,
             'Asia': asia,
             'europe' : europe
             }
    return render(request, 'chart_bar.html', context)


def wordcloud(request):
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean bibendum erat ac justo sollicitudin, quis lacinia ligula fristo nunc pretium hendrerit. ';

    context ={'text':text}
    return render(request, 'chart_wordcloud.html', context)


def ajax(request):

    return render(request, 'chart_ajax.html')
















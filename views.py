from django.shortcuts import render, redirect
from .models import Student, ExamSession, Reservation
from django.utils import timezone

def register_exam(request):
    if request.method == 'POST':
        # Get data from form submission
        student_name = request.POST['studentName']
        student_nshe = request.POST['studentNSHE']
        exam_type = request.POST['examType']
        exam_session_id = request.POST['examSession']
        timestamp = timezone.now()

        # Retrieve student and exam session
        student = Student.objects.get(nshe_number=student_nshe)
        session = ExamSession.objects.get(id=exam_session_id)

        # Check if session is full
        if session.available_seats > 0:
            # Register the student
            session.available_seats -= 1
            session.save()
            reservation = Reservation.objects.create(student=student, session=session, registration_time=timestamp)

            return redirect('confirmation')
        else:
            return render(request, 'registration/register.html', {
                'error': 'The session is full. Please select another session.'
            })
    else:
        # Retrieve available exams and sessions for GET requests
        exams = Exam.objects.all()
        sessions = ExamSession.objects.filter(available_seats__gt=0)

        return render(request, 'registration/register.html', {
            'exams': exams,
            'sessions': sessions,
        })

def confirmation_page(request):
    return render(request, 'registration/confirmation.html')

# Postman Collection for AMEP API Testing

## Base URL
`http://localhost:8000/api`

## Students API

### Get Student Profile
```
GET /students/profile/{student_id}
Response:
{
  "id": 1,
  "email": "student@example.com",
  "name": "John Doe",
  "role": "student"
}
```

### Get Student Mastery
```
GET /students/{student_id}/mastery
Response:
{
  "student_id": 1,
  "mastery_profiles": [
    {
      "concept": "Algebra",
      "mastery_score": 75.5,
      "attempt_count": 10,
      "correct_count": 8
    }
  ]
}
```

### Get Student Assignments
```
GET /students/{student_id}/assignments
Response:
{
  "assignments": [
    {
      "id": 1,
      "concept": "Calculus",
      "difficulty_level": 3,
      "completed": false,
      "score": null
    }
  ]
}
```

## Teachers API

### Get Teacher Dashboard
```
GET /teachers/{teacher_id}/dashboard
Response:
{
  "total_students": 25,
  "avg_mastery": 72.5,
  "engagement_index": 85.0,
  "confusion_index": 18.5
}
```

### Create Poll
```
POST /teachers/{teacher_id}/poll/create
Body:
{
  "question": "Do you understand this concept?",
  "options": ["Strongly Agree", "Agree", "Disagree"]
}
Response:
{
  "poll_id": 1,
  "message": "Poll created"
}
```

### Get Poll Results
```
GET /teachers/{teacher_id}/poll/{poll_id}/results
Response:
{
  "poll_id": 1,
  "responses": 25,
  "results": {
    "option_a": 40,
    "option_b": 60
  }
}
```

## Engagement API

### Track Engagement
```
POST /engagement/track
Body:
{
  "student_id": 1,
  "course_id": 1,
  "poll_response": {"question_1": "answer_a"},
  "confusion_index": 25.5,
  "participation_type": "explicit"
}
Response:
{
  "record_id": 1,
  "message": "Engagement tracked"
}
```

### Get Class Engagement Summary
```
GET /engagement/class/{course_id}/summary
Response:
{
  "course_id": 1,
  "total_responses": 25,
  "avg_confusion_index": 22.3,
  "participation_rate": 96.0
}
```

## Mastery API

### Update Mastery Score
```
POST /mastery/update
Body:
{
  "student_id": 1,
  "concept": "Algebra",
  "correct": true,
  "difficulty": 3
}
Response:
{
  "student_id": 1,
  "concept": "Algebra",
  "new_mastery_score": 78.5
}
```

### Get Weak Concepts
```
GET /mastery/{student_id}/weak-concepts
Response:
{
  "student_id": 1,
  "weak_concepts": [
    {
      "concept": "Calculus",
      "mastery_score": 45.0,
      "zpd_level": 3
    }
  ]
}
```

### Generate Adaptive Homework
```
POST /mastery/{student_id}/generate-homework
Response:
{
  "student_id": 1,
  "generated_assignments": [
    {
      "concept": "Calculus",
      "difficulty_level": 3
    }
  ]
}
```

## Assessments API

### Submit Assessment
```
POST /assessments/submit
Body:
{
  "student_id": 1,
  "course_id": 1,
  "concepts": {
    "Algebra": 85,
    "Geometry": 72,
    "Calculus": 45
  },
  "score": 67.3
}
Response:
{
  "assessment_id": 1,
  "message": "Assessment submitted successfully"
}
```

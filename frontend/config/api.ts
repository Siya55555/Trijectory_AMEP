/**
 * Frontend API Configuration
 */

export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

export const API_ENDPOINTS = {
  // Students
  STUDENT_PROFILE: (id: number) => `/students/profile/${id}`,
  STUDENT_MASTERY: (id: number) => `/students/${id}/mastery`,
  STUDENT_ASSIGNMENTS: (id: number) => `/students/${id}/assignments`,
  
  // Teachers
  TEACHER_DASHBOARD: (id: number) => `/teachers/dashboard/${id}`,
  TEACHER_STUDENTS: (id: number) => `/teachers/${id}/students`,
  CREATE_POLL: (id: number) => `/teachers/${id}/poll/create`,
  GET_POLL_RESULTS: (id: number, pollId: number) => `/teachers/${id}/poll/${pollId}/results`,
  
  // Engagement
  TRACK_ENGAGEMENT: '/engagement/track',
  ENGAGEMENT_SUMMARY: (courseId: number) => `/engagement/class/${courseId}/summary`,
  ENGAGEMENT_HISTORY: (studentId: number) => `/engagement/${studentId}/history`,
  
  // Mastery
  UPDATE_MASTERY: '/mastery/update',
  GET_WEAK_CONCEPTS: (id: number) => `/mastery/${id}/weak-concepts`,
  GENERATE_HOMEWORK: (id: number) => `/mastery/${id}/generate-homework`,
  
  // Assessments
  SUBMIT_ASSESSMENT: '/assessments/submit',
  GET_ASSESSMENT: (id: number) => `/assessments/${id}`,
};

export const API_TIMEOUT = 10000; // 10 seconds

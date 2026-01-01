/**
 * Global Type Definitions for AMEP Frontend
 */

// Student Types
export interface Student {
  id: number;
  email: string;
  name: string;
  role: 'student';
}

export interface MasteryProfile {
  concept: string;
  mastery_score: number;
  attempt_count: number;
  correct_count: number;
}

export interface Assignment {
  id: number;
  concept: string;
  difficulty_level: number;
  completed: boolean;
  score: number | null;
}

// Teacher Types
export interface TeacherDashboard {
  total_students: number;
  avg_mastery: number;
  engagement_index: number;
  confusion_index: number;
}

export interface Poll {
  poll_id: number;
  question: string;
  responses: number;
  results: Record<string, number>;
}

// Engagement Types
export interface EngagementRecord {
  student_id: number;
  course_id: number;
  poll_response: Record<string, string>;
  confusion_index: number;
  participation_type: 'explicit' | 'implicit';
}

export interface EngagementSummary {
  course_id: number;
  total_responses: number;
  avg_confusion_index: number;
  participation_rate: number;
}

// Assessment Types
export interface Assessment {
  id: number;
  student_id: number;
  course_id: number;
  score: number;
  concepts: Record<string, number>;
  timestamp: string;
}

// API Response Types
export interface ApiResponse<T> {
  data?: T;
  message?: string;
  error?: string;
  status: 'success' | 'error';
}

// Project Types
export interface Project {
  id: number;
  title: string;
  description: string;
  status: 'active' | 'completed' | 'archived';
  progress: number;
}

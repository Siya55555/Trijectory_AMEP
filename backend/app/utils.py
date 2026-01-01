"""
Utilities for AMEP Platform
"""

def calculate_zpd_level(mastery_score: float) -> int:
    """
    Calculate Zone of Proximal Development level based on mastery score
    
    Args:
        mastery_score: Student's mastery score (0-100)
        
    Returns:
        ZPD level (1-5): 1=easy, 5=hard
    """
    if mastery_score >= 80:
        return 5
    elif mastery_score >= 60:
        return 4
    elif mastery_score >= 40:
        return 3
    elif mastery_score >= 20:
        return 2
    else:
        return 1

def get_engagement_status(engagement_index: float) -> str:
    """
    Get engagement status based on index value
    
    Args:
        engagement_index: Engagement index (0-100)
        
    Returns:
        Status string
    """
    if engagement_index >= 80:
        return "Highly Engaged"
    elif engagement_index >= 60:
        return "Engaged"
    elif engagement_index >= 40:
        return "Moderately Engaged"
    else:
        return "At Risk"

def assess_concept_mastery(correct_count: int, attempt_count: int) -> float:
    """
    Calculate concept mastery percentage
    
    Args:
        correct_count: Number of correct attempts
        attempt_count: Total number of attempts
        
    Returns:
        Mastery percentage (0-100)
    """
    if attempt_count == 0:
        return 0.0
    return (correct_count / attempt_count) * 100

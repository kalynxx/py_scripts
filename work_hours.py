def calculate_work_hours(start_time=None, end_time=None):
    """Calculate work hours minus 45 minutes break time if worked 5+ hours."""
    
    
    print("\n*** Work Hours Calculator ***\n")
    
    try:
        if start_time is None:
            start_time = input("Enter start time (HH:MM): ")
        if end_time is None:
            end_time = input("Enter end time (HH:MM): ")
        
        # Parse times
        start_h, start_m = map(int, start_time.split(':'))
        end_h, end_m = map(int, end_time.split(':'))
        
        # Convert to minutes
        start_total: int = start_h * 60 + start_m
        end_total: int = end_h * 60 + end_m
        
        # Handle next day scenario
        if end_total < start_total:
            end_total += 24 * 60
        
        # Calculate worked minutes
        worked_minutes: int = end_total - start_total
        worked_hours: float = worked_minutes / 60
        
        # Deduct 45 minutes if worked 5+ hours
        if worked_hours >= 5:
            worked_minutes -= 45
        
        # Convert back to hours and minutes
        final_hours: int = worked_minutes // 60
        final_minutes: int = worked_minutes % 60
        
        print(f"Total worked: {worked_hours:.2f} hours")
        print(f"Break deducted: {'45 minutes' if worked_hours >= 5 else 'None'}")
        
        final: str = f"\nFinal work hours: {final_hours:.0f}h {final_minutes:.0f}m ({worked_minutes/60:.2f} hours)"
        for i in range(len(final) - 1):
            print("-", end='', flush=True)

        print(final)
        
    except ValueError:
        print("Invalid time format. Please use HH:MM format.")

if __name__ == "__main__":
    import sys
    
    start_time = sys.argv[1] if len(sys.argv) > 1 else None
    end_time = sys.argv[2] if len(sys.argv) > 2 else None
    
    calculate_work_hours(start_time, end_time)
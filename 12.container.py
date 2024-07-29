def solution(queries):
    container = set()
    results = []
    
    for query in queries:
        command, value = query
        if command == "ADD":
            container.add(value)
        elif command == "EXISTS":
            if value in container:
                results.append("true")
            else:
                results.append("false")
    
    return results

# Example usage
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "5"],
    ["ADD", "2"],
    ["EXISTS", "2"],
    ["EXISTS", "5"],
    ["EXISTS", "1"],
    ["EXISTS", "4"],
    ["EXISTS", "3"],
    ["EXISTS", "0"]
]
print(solution(queries))
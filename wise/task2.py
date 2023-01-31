def getRequestStatus(requests):
    result = []
    result.append('{status: 200, message: OK}')
    
    for i in range(1, len(requests)):
        if requests[max(i-30, 0):i].count(requests[i]) >= 5:
            result.append('{status: 429, message: Too many requests}')
            requests[i] = ""
            continue
        if requests[max(i-5, 0):i].count(requests[i]) >= 2:
            result.append('{status: 429, message: Too many requests}')
            requests[i] = ""
            continue
        
        result.append('{status: 200, message: OK}')
    return result

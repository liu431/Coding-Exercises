class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_list = []
        for email in emails:
            parts = email.split('@')
            local, domain = parts[0], parts[1]
            local = local.replace('.', '')
            if '+' in local:
                local = local.split('+')[0]
            email_list.append(local+'@'+domain)
        return len(set(email_list))
        

from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    parents = []
    ans = []
    for file in files: 
        if file.parent not in parents:
            parents.append(file.parent)
    for file in files:
        if file.id not in parents:
            ans.append(file.name)

    return ans


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    category_map = {}; 
    for file in files:
        for category in file.categories:
            if category not in category_map:
                category_map[category]= 1
            else:
                category_map[category] += 1

    sorted_files = sorted(category_map.items(), key=lambda x: (-x[1], x[0]))

    return [category[0] for category in sorted_files[:k]]



"""
Task 3
"""

def recurse(adjacency, file):
    if file.id not in adjacency or len(adjacency[file.id]) == 0:
        return file.size

    total = 0
    for f in adjacency[file.id]:
        total += recurse(adjacency, f)
    
    return total
        


def largestFileSize(files: list[File]) -> int:
    mp = {}
    for file in files:
        if file.parent in mp:
            mp[file.parent].append(file)
        else:
            mp[file.parent] = [file]
    
    ans = 0
    for file in files:
        ans = max(ans, recurse(mp, file))

    
    return ans





if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]


    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992

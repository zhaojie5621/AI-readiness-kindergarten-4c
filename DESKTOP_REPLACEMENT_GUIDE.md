# One-time repository replacement using GitHub Desktop

1. Open the cloned repository in Windows Explorer from GitHub Desktop:
   **Repository → Show in Explorer**.
2. Delete every file and folder inside that cloned repository folder, except the hidden `.git` folder.
3. Extract this package elsewhere.
4. Copy all extracted files and folders into the now-empty cloned repository folder.
5. Return to GitHub Desktop.
6. Commit with: `Replace repository with corrected structure`.
7. Click **Push origin**.
8. Refresh the repository webpage.

Deleting the online files through this commit does not erase old commit history. It replaces the current `main` branch contents.

<?php
// NETS Content Hub - Live Folder Scanner for Hostinger
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Cache-Control: no-cache, no-store, must-revalidate');
header('Pragma: no-cache');
header('Expires: 0');

$results = [];

// Recursively scan all Cluster-* directories for .md and .html files
function scanDirectory($dir, &$results) {
    if (!is_dir($dir)) return;
    $items = scandir($dir);
    if ($items === false) return;
    
    foreach ($items as $item) {
        if ($item === '.' || $item === '..' || $item[0] === '.') continue;
        $fullPath = $dir . '/' . $item;
        
        if (is_dir($fullPath)) {
            scanDirectory($fullPath, $results);
        } elseif (is_file($fullPath)) {
            $ext = strtolower(pathinfo($fullPath, PATHINFO_EXTENSION));
            if ($ext === 'md' || $ext === 'html' || $ext === 'htm') {
                $relDir = dirname($fullPath);
                $dirParts = explode('/', str_replace('\\', '/', $relDir));
                $clusterFolder = $dirParts[0] ?? 'Cluster-01';
                $weekFolder = count($dirParts) > 1 ? implode('/', array_slice($dirParts, 1)) : 'General';
                
                $content = @file_get_contents($fullPath);
                if ($content !== false) {
                    $results[] = [
                        'path' => $fullPath,
                        'filename' => basename($fullPath),
                        'cluster' => $clusterFolder,
                        'clusterFolder' => $clusterFolder,
                        'week' => $weekFolder,
                        'weekFolder' => $weekFolder,
                        'size' => filesize($fullPath),
                        'lastModified' => filemtime($fullPath),
                        'content' => $content
                    ];
                }
            }
        }
    }
}

// Find all Cluster-* directories (case-insensitive and plural-tolerant)
$clusterDirs = glob('{Cluster-*,cluster-*,Clusters-*,clusters-*}', GLOB_BRACE | GLOB_ONLYDIR);
if (empty($clusterDirs)) {
    $allDirs = glob('*', GLOB_ONLYDIR);
    $clusterDirs = array_values(array_filter($allDirs ?: [], function($d) {
        return stripos($d, 'cluster') !== false;
    }));
}
if (!empty($clusterDirs)) {
    foreach ($clusterDirs as $cDir) {
        scanDirectory($cDir, $results);
    }
}

// Sort alphabetically by path
usort($results, function($a, $b) {
    return strcmp($a['path'], $b['path']);
});

echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);

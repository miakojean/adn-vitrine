export function useAnalytics() {
    const trackEvent = (eventName: string, data?: Record<string, any>) => {
        // Implémentation de votre service d'analytics
        console.log(`[Analytics] ${eventName}:`, data);
        
        // Exemple avec Google Analytics
        
    };
    
    return {
        trackEvent
    };
}
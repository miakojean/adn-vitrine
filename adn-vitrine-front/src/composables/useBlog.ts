import { ref, computed } from 'vue';

interface Category {
    id: string;
    label: string;
    count: number;
}

interface Article {
    id: string;
    title: string;
    excerpt: string;
    imageSrc: string;
    link: string;
    category: string;
    date: string;
    readTime: string;
    isFeatured?: boolean;
}

export function useBlog() {
    // State
    const categories = ref<Category[]>([
        { id: 'all', label: 'Tous', count: 12 },
        { id: 'legal', label: 'Juridique', count: 5 },
        { id: 'tech', label: 'Technologie', count: 4 },
        { id: 'business', label: 'Business', count: 3 }
    ]);
    
    const articles = ref<Article[]>([]);
    const selectedCategory = ref('all');
    const isLoading = ref(false);
    
    // Computed
    const filteredArticles = computed(() => {
        if (selectedCategory.value === 'all') return articles.value;
        return articles.value.filter(article => 
            article.category === selectedCategory.value
        );
    });
    
    // Methods
    const fetchArticles = async () => {
        isLoading.value = true;
        try {
            // Simulation d'API call
            await new Promise(resolve => setTimeout(resolve, 500));
            
            // Données mockées
            articles.value = [
                {
                    id: '1',
                    title: 'Transformation numérique dans le droit',
                    excerpt: 'Découvrez comment la transformation numérique révolutionne le secteur juridique en améliorant l\'efficacité.',
                    imageSrc: 'https://picsum.photos/400/300',
                    link: '#',
                    category: 'tech',
                    date: '2024-01-15',
                    readTime: '5 min',
                    isFeatured: true
                },
                // ... ajouter plus d'articles
            ];
        } catch (error) {
            console.error('Error fetching articles:', error);
        } finally {
            isLoading.value = false;
        }
    };
    
    const setCategory = (categoryId: string) => {
        selectedCategory.value = categoryId;
    };
    
    return {
        categories,
        articles,
        selectedCategory,
        filteredArticles,
        isLoading,
        fetchArticles,
        setCategory
    };
}
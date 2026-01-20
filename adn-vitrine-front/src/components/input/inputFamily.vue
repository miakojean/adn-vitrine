<template>
    <div class="input__family">
        <label 
            v-if="label" 
            :for="name" 
            class="input__label"
        >
            {{ label }}
        </label>
        <input 
            :type="type" 
            :name="name" 
            :id="name" 
            :placeholder="placeholder" 
            :required="required" 
            class="input__field"
            :value="modelValue"
            @input="updateValue($event)"
        />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'InputFamily',
    props: {
        type: {
            type: String,
            default: 'text'
        },
        name: {
            type: String,
            required: true
        },
        label: {
            type: String,
            default: ''
        },
        placeholder: {
            type: String,
            default: ''
        },
        required: {
            type: Boolean,
            default: false
        },
        modelValue: { // Convention v-model
            type: [String, Number],
            default: ''
        }
    },
    emits: ['update:modelValue'],
    methods: {
        updateValue(event: Event) {
            const target = event.target as HTMLInputElement;
            let value: string | number = target.value;
            
            // Gestion des nombres
            if (this.type === 'number') {
                if (value === '') {
                    // Pour permettre le champ vide
                    this.$emit('update:modelValue', '');
                } else {
                    const numValue = parseFloat(value);
                    if (!isNaN(numValue)) {
                        value = numValue;
                    }
                }
            }
            
            this.$emit('update:modelValue', value);
        }
    }
});
</script>

<style scoped>
.input__family {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}
input{
    padding: 1rem;
    width: 100%;
    color: #dfecfd;
    border: 1px solid #dae5f2;
    border-radius: 0.5rem;
    outline: #A7CEFD;
}
label{
    font-weight: 600;
}
</style>
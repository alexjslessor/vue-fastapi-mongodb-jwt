<template>
    <!-- <v-data-table :headers="tableHeaders" :items="tableItems" :items-per-page="5" class="elevation-1"> -->
    <v-data-table v-bind='$attrs' v-on='$listeners'>

        <template v-slot:top>
            <!-- <ToolbarHeader title='Master Table'>
                <v-spacer></v-spacer>
                <v-btn small color='primary'></v-btn>
            </ToolbarHeader> -->
            <slot name='top' />
        </template>


    </v-data-table>
</template>
<script>
    import ToolbarHeader from '@/components/fragments/ToolbarHeader'
    export default {
        components: { ToolbarHeader },
        props: {
            tableHeaders: {
                type: Array,
                required: false
            },
            tableItems: {
                type: Array,
                required: false
            },
            // rowsPerPage: {
            //     type: String,
            //     required: false
            // },
        },
        data() {
            return {}
        },
    }
</script>